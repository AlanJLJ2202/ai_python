import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score


data = pd.read_cv("credit_data.csv") #load dataset

features = data[["income", "age", "loan"]] #attributes to be used in the model
target = data.default #labels of dataset

#convert dataframes to np arrays
x = np.array(features).reshape(-1, 3)
y = np.array(target)

# perform normalization
x = preprocessing.MinMaxScaler().fit_transform(x)


# split dataset between training-testing
training_dataset, testing_dataset, training_dataset, testing_target = train_test_split(x, y, test_size=0.3)


# create KNN model
model = KNeighborsClassifier(n_neighbors=7)
fitted_model = model.fit(training_dataset, testing_target)

predict = fitted_model.predict(np.array([[100000, 50, 6000]]))
print(predict)


#many predictions
predictions = fitted_model.predict(testing_dataset)
print(confusion_matrix(testing_target, predictions))
#print(accuracy_matrix)
print(accuracy_score(testing_target, predictions))

#Estudiar 
for k in range(1, 100):

    # perform crossvalidation
    knn = KNeighborsClassifier(6)
    scores = cross_val_score(knn, x, y, cv=10, scoring="accuracy")

    print(scores)
    print(np.mean(scores))






