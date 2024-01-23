import matplotlib
matplotlib.use('Agg')

import sys
sys.path.append('..')

from torchvision import transforms
import torch
import lightning.pytorch as pl
from net import Net 
import base64 
from io import BytesIO 
from PIL import Image
import os
import matplotlib.pyplot as plt


# Set to model version to load
version = 1 

name = os.listdir(f'../lightning_logs/version_{version}/checkpoints')[0]
checkpoint = f'../lightning_logs/version_{version}/checkpoints/{name}'

net = Net.load_from_checkpoint(checkpoint)

transform = transforms.Compose([
	transforms.Resize(28),
	transforms.CenterCrop([28,28]),
	transforms.ToTensor(),
])

def preprocess_img(img):
	data = img.split(b',')[-1]
	image_data = base64.decodebytes(data)
	image = Image.open(BytesIO(image_data))
	transformed_img = transform(image)

	return transformed_img

def get_prediction(img):

	img = preprocess_img(img)
	img = torch.reshape(img[3], [1,28,28])

	output = net(img.unsqueeze(0))
	predicted = int(torch.argmax(output))

	return predicted