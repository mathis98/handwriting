import lightning.pytorch as pl
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class Net(pl.LightningModule):
	def __init__(self):
		super(Net, self).__init__()

		self.conv1 = nn.Conv2d(1, 32, 3, 1)
		self.conv2 = nn.Conv2d(32, 64, 3, 1)
		self.dropout1 = nn.Dropout(.25)
		self.dropout2 = nn.Dropout(.5)
		self.fc1 = nn.Linear(9216, 128)
		self.fc2 = nn.Linear(128, 10)

		self.test_nll = []

	def forward(self, x):

		# Convolution 1
		x = self.conv1(x)
		x = F.relu(x)

		# Convolution 2
		x = self.conv2(x)
		x = F.relu(x)
		x = F.max_pool2d(x, 2)
		x = self.dropout1(x)
		x = torch.flatten(x, 1)

		# Fully Connected 1
		x = self.fc1(x)
		x = F.relu(x)
		x = self.dropout2(x)

		# Fully Connected 2
		x = self.fc2(x)

		# To probabilities
		output = F.log_softmax(x, dim=1)

		return output

	def training_step(self, batch, batch_idx):
		data, target = batch

		output = self(data)
		loss = F.nll_loss(output, target)

		self.log('train-loss', loss, prog_bar=True)

		return loss

	def test_step(self, batch, batch_idx):
		data, target = batch

		output = self(data)
		loss = F.nll_loss(output, target, reduction='none')

		avg_loss = loss.mean()

		self.log('test-loss', avg_loss, prog_bar=True)

		self.test_nll.extend(loss.detach().cpu().numpy())

	def on_test_epoch_end(self):
		avg_loss = np.mean(self.test_nll)
		self.log('avg_test-loss', avg_loss, prog_bar=True)
		self.test_nll = []

	def configure_optimizers(self):
		optimizer = torch.optim.AdamW(self.parameters())

		return optimizer