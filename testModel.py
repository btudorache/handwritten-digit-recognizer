import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test_examples, x_test_width, x_test_height = x_test.shape
x_test = x_test.reshape(x_test_examples, x_test_width, x_test_height, 1)


model = tf.keras.models.load_model('model')
print()

model.summary()
print()

loss, acc = model.evaluate(x_test, y_test, verbose=2)
print()

print('Model accuracy: {:5.2f}%'.format(100 * acc))
print()

predictions = model.predict(x_test)

wrong_predictions_num = 0
wrong_predictions_list = []
for i in range(len(predictions)):
    if np.argmax(predictions[i]) != y_test[i]:
        wrong_predictions_num += 1
        image_information = (i, np.argmax(predictions[i]), y_test[i])
        wrong_predictions_list.append(image_information)

print(f"Out of {len(y_test)} digit pictures, there were {wrong_predictions_num} wrong predictions")
print()

print("The wrong predicted images will be shown. Close the image to see the next one")
print()

shuffle(wrong_predictions_list)

for i, predicted_value, actual_value in wrong_predictions_list:
    print(f"This image is predicted to be a {predicted_value} but it's actually labeled as {actual_value}")
    plt.figure()
    plt.imshow(x_test[i])
    plt.colorbar()
    plt.grid(False)
    plt.show()
