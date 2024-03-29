# Handwritten Digit Recognizer 

Implementation of a digit drawer and recognition software for numbers 0 through 9. It uses a Convolutional Neuronal Network model implemented in **tensorflow** 
and trained on the *MNIST dataset*. The architecture of the network is a classic CNN one, with convolution and pooling layers connected to a final 10 node layer, one for each of the 10 digits.

The model has a **~99% accuracy** on the *MNIST testset (10.000 samples)*.

## Requirements

**Python 3.8.0** and **pip version > 19.0** are required for installing the requirements. Main packages used:

* Tensorflow2

* Matplotlib

* Numpy

* Pygame

## Setup - Ubuntu/MacOS Terminal

Clone the repository locally. Optionally use a virtual env:
```
python3 -m venv venv         # create venv
source venv/bin/activate     # activate venv
```

Install the requirements:
```
pip3 install -r requirements.txt
```

## Usage

Test the actual trained model. You can also see which images were incorrectly labelled on the testset:
```
python3 testModel.py
```

Run the digit drawer:
```
python3 digitPainter.py
```
Click and draw a digit. Press ```SPACEBAR``` to evaluate the picture.


You can also train a new model:
```
python3 createModel.py
```

## Media

Drawing and tesing a 2:

![2_drawing](https://github.com/btudorache/handwritten-digit-recognizer/blob/master/readme_media/2_drawing.PNG)

Drawing and testing a 5:

![5_drawing](https://github.com/btudorache/handwritten-digit-recognizer/blob/master/readme_media/5_drawing.PNG)


