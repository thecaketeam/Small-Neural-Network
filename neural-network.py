import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
mnist_train = pd.read_csv("mnist_train.csv", header=None)
mnist_test = pd.read_csv("mnist_test.csv", header=None)
cols = ["label"]

for i in range(784):
    cols.append(f"px_{i + 1}")
mnist_train.columns = cols
mnist_test.columns = cols
image_size = 28 #Size of picture
train_label = mnist_train["label"].values
test_label = mnist_test["label"].values
train_image = mnist_train.values[:, 1:]
test_image = mnist_test.values[:, 1:]
train_image = train_image.reshape(100, 28, 28)
test_image = test_image.reshape(10, 28, 28)
knn_classifier = KNeighborsClassifier(n_jobs=-1)
plt.imshow(train_image[0,:],cmap="Greys")
knn_classifier = knn_classifier.fit(train_image.reshape(100,784),train_label)
image_id = 2
prediction = knn_classifier.predict(test_image[image_id].reshape(1,784))
plt.imshow(test_image[image_id],cmap="Greys")
all_predictions = knn_classifier.predict(test_image.reshape(10,784))
accuracy_score(test_label, all_predictions) * 100
cm = confusion_matrix(test_label, all_predictions)
cm
for i, (real, pred) in enumerate(zip(test_label, all_predictions)):
    if real == 4 and real != pred:
        print(f"Prediction: {pred}")
        plt.imshow(test_image[i], cmap="Greys")
        plt.show()
nn_classifier = MLPClassifier(verbose=True)
nn_classifier = nn_classifier.fit(test_image.reshape(10,784), test_label)
all_predictions = knn_classifier.predict(test_image.reshape(10,784))
accuracy_score(test_label, all_predictions) * 100
cm = confusion_matrix(test_label, all_predictions)
cm
for i, (real, pred) in enumerate(zip(test_label, all_predictions)):
    if real == 4 and real != pred:
        print(f"Prediction: {pred}")
        plt.imshow(test_image[i], cmap="Greys")
        plt.show()
