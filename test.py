from torchvision import datasets, transforms
import os
import torch
import lightning.pytorch as pl
from net import Net 
import random
import matplotlib.pyplot as plt


version = 1

name = os.listdir(f'./lightning_logs/version_{version}/checkpoints')[0]
checkpoint = f'./lightning_logs/version_{version}/checkpoints/{name}'

net = Net.load_from_checkpoint(checkpoint)

transform = transforms.Compose([
	transforms.ToTensor(),
	transforms.Normalize((.1307,),(.3081,))
])

test_data = datasets.MNIST('./data', train=False, download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=64)


indeces = random.sample(range(len(test_data)), 5)

random_elems = [test_data[i] for i in indeces]

fig, axes = plt.subplots(1, 5, figsize=(9,3))

for idx, elem in enumerate(random_elems):

	img, target = elem
	output = net(img.unsqueeze(0))

	predicted = int(torch.argmax(output))

	img = img.reshape(28,28)

	color = 'g' if predicted == target else 'r'

	axes[idx].set_title(f'{predicted} ({target})', color=color)
	axes[idx].imshow(img,cmap='gray')
	axes[idx].axis('off')

plt.show()