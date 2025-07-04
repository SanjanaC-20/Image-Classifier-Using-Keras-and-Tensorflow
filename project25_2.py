# -*- coding: utf-8 -*-
"""Project25_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vV_-0GFPBrGoFpN-yRabaH-JKT5HWnLP
"""

//image classifier using keras and tenserflow

import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

datasets.mnist.load_data()

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

train_images = train_images/255.0
test_images = test_images/255.0

train_images = train_images.reshape((train_images.shape[0], 28,28,1))
test_images = test_images.reshape((test_images.shape[0], 28,28,1))

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers. Conv2D(32, (3,3), activation= 'relu', input_shape=(28,28,1)))

model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation= 'relu'))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3,3), activation= 'relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation= 'relu'))
model.add(layers.Dense(10, activation= 'softmax'))
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics= ['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

test_loss , test_acc = model.evaluate(test_images, test_labels)
print(test_acc)

predictions = model.predict(test_images)
print(f"Predicted: {np.argmax(predictions[0])}")



plt.imshow(test_images[0].reshape(28,28), cmap = 'gray')
plt.show()