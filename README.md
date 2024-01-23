# Handwritten Character Recognition
Simple MNIST trained handwriting recognition model using CNN with webpage playground. The network consists of two convolutional layers followed by two fully-connected layers for classification with softmax. It uses the negative log likelihood loss. It is a quite simple architecture. I opted for a modern pytorch lightning implementation so this architecture is easily adaptable. Furthermore I added a simple webpage with a flask backend to interactively check the model. It is therefore easy to interactively experiment with differing model architectures.

Run **main.py** to train model which is then checkpointed

Run **test.py** to see example predictions on randomly drawn digits on trained model (set version to match the version you want to load).

Run **flask --app server run** in the web directory to launch an interactive website that allows to draw a digit that gets predicted by the model (set version to match the version you want to load).

## Example

<img width="400" height="400" src="example recording.gif" alt="example recording" />
