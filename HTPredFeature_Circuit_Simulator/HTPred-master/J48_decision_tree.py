import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics


f = open("headers.txt", "r")
x = f.read()
f.close()


list_features = x.split(",")
list_features.pop(-1)
list_features.pop(0)
list_features.append("Label")
print(list_features)

list_features1 = list_features[:]

col_names = list_features
# # load dataset
pima = pd.read_csv("data_21_05_2021.csv", header=None, names=col_names)

del list_features1[-1]

feature_cols = list_features1
X = pima[feature_cols]
y = pima.Label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
