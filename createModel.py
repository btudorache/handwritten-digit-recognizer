import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train_examples, x_train_width, x_train_height = x_train.shape
x_train = x_train.reshape(x_train_examples, x_train_width, x_train_height, 1)

x_test_examples, x_test_width, x_test_height = x_test.shape
x_test = x_test.reshape(x_test_examples, x_test_width, x_test_height, 1)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (5, 5), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Conv2D(32, (5, 5), activation='relu'),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Conv2D(64, (4, 4)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['sparse_categorical_accuracy'])

model.fit(x_train, y_train, epochs=7)
model.evaluate(x_test,  y_test, verbose=2)

model.save('model')