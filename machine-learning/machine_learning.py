# Machine Learning Models
from sklearn.model_selection import train_test_split
from sklearn import datasets, svm
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
)

#Models

# SVM (with iris dataset)
iris = datasets.load_iris()

X = iris.data[:, :4]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)



C = 1.0  # SVM regularization parameter
models = (
    svm.SVC(kernel="linear", C=C),
    svm.LinearSVC(C=C, max_iter=10000),
    svm.SVC(kernel="rbf", gamma=0.6, C=C),
    svm.SVC(kernel="poly", degree=3, gamma="auto", C=C),
)

models = list(clf.fit(X_train, y_train) for clf in models)

clf1, clf2, clf3, clf4 = models

y_pred1 = clf1.predict(X_test)
y_pred2 = clf2.predict(X_test)
y_pred3 = clf3.predict(X_test)
y_pred4 = clf4.predict(X_test)

# Evaluate the model

# Model 1
accuracy = accuracy_score(y_test, y_pred1)
mse1 = mean_squared_error(y_test, y_pred1)
mae1 = mean_absolute_error(y_test, y_pred1)
r21 = r2_score(y_test, y_pred1)

# Model 2
accuracy = accuracy_score(y_test, y_pred2)
mse2 = mean_squared_error(y_test, y_pred2)
mae2 = mean_absolute_error(y_test, y_pred2)
r22 = r2_score(y_test, y_pred2)

# Model 3
accuracy = accuracy_score(y_test, y_pred3)
mse3 = mean_squared_error(y_test, y_pred3)
mae3 = mean_absolute_error(y_test, y_pred3)
r23 = r2_score(y_test, y_pred3)

# Model 4
accuracy = accuracy_score(y_test, y_pred4)
mse4 = mean_squared_error(y_test, y_pred4)
mae4 = mean_absolute_error(y_test, y_pred4)
r24 = r2_score(y_test, y_pred4)
