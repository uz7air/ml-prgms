import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

# Load and prepare data
data = pd.read_csv('lab6.csv', names=['Age', 'Gender', 'Familylist', 'Diet', 'LifeStyle', 'Cholesterol', 'heartDisease'])
data = data.apply(LabelEncoder().fit_transform)  # Encode all columns

# Separate features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model and predict
clf = GaussianNB().fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Print confusion matrix
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
