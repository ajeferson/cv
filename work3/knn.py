import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Importing dataset
dataset = pd.read_csv("dataset.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting dataset into trainning set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=42)

# Feature scalling (standardisation)
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

# Euclidian distance
classifier = KNeighborsClassifier(n_neighbors=5, p=2)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print 'Confusion Matrix:'
print cm

print '\nAccuracy:', acc
