from flask import Flask, request, render_template
from utility import get_prediction

app = Flask(__name__)

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		file = request.data

		prediction = get_prediction(file)

		return f'{prediction}'