from torchvision import datasets, transforms
import lightning.pytorch as pl
from lightning.pytorch.callbacks import ModelCheckpoint
import torch
import torch.nn as nn
import torch.nn.functional as F
from net import Net


transform = transforms.Compose([
	transforms.ToTensor(),
	transforms.Normalize((.1307,),(.3081,))
])

train_data = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('./data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=64)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=64)


net = Net()

trainer = pl.Trainer(
	max_epochs=14, 
	callbacks=[
		ModelCheckpoint(),
	]
,)

trainer.fit(net, train_loader)

trainer.test(ckpt_path='best', dataloaders=test_loader)