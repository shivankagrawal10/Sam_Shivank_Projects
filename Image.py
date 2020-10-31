#import tensorflow as tf
import math
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from keras.utils import np_utils
import cv2

from wand.image import Image as Img
from wand.color import Color

def importPdf(self):
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",
                                                        QtCore.QDir.currentPath())
    print(filename)
    if not filename:
        print('error')
        return
    with Img(filename=filename,format='jpeg', resolution=300) as image:
        image.compression_quality = 99
        image.save(filename='file.jpeg')
        self.open_picture()


def create_training_data():
    #image = cv2.imread('1.jpg')

    #default_file = 'sudoku.png'
    # Loads an image
    #src = cv2.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)

    from PIL import Image
    import numpy
    #image = Image.open('1.jpeg')
    image = '1.jpeg'
    #print (image)
    #src = cv2.imread(cv2.samples.findFile('1.jpg'), cv2.IMREAD_GRAYSCALE)
    src = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    matrix = cv2.HoughLines(src, 1, math.pi / 180,30)
    
    #import pandas as pd 
    #pd.DataFrame(matrix[:][:][0]).to_csv("matrix.csv")
    print(matrix)

create_training_data()
#train()
def train():
    ''' Source: https://www.analyticsvidhya.com/blog/2020/02/learn-image-classification-cnn-convolutional-neural-networks-3-datasets/'''

    # to calculate accuracy
    from sklearn.metrics import accuracy_score

        # loading the dataset
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # building the input vector from the 28x28 pixels
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
    X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')

    # normalizing the data to help with the training
    X_train /= 255
    X_test /= 255

    # one-hot encoding using keras' numpy-related utilities
    n_classes = 10
    print("Shape before one-hot encoding: ", y_train.shape)
    Y_train = np_utils.to_categorical(y_train, n_classes)
    Y_test = np_utils.to_categorical(y_test, n_classes)
    print("Shape after one-hot encoding: ", Y_train.shape)

    # building a linear stack of layers with the sequential model
    model = Sequential()
    # convolutional layer
    model.add(Conv2D(25, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu', input_shape=(28,28,1)))
    model.add(MaxPool2D(pool_size=(1,1)))
    # flatten output of conv
    model.add(Flatten())
    # hidden layer
    model.add(Dense(100, activation='relu'))
    # output layer
    model.add(Dense(10, activation='softmax'))

    # compiling the sequential model
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

    # training the model for 10 epochs
    model.fit(X_train, Y_train, batch_size=128, epochs=1, validation_data=(X_test, Y_test))
    #model.predict(cv2.imread("1.jpeg"))
    import pydot
    from keras.utils.vis_utils import plot_model
    #plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
    tf.keras.utils.plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)