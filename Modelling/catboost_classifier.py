import pandas as pd
import xgboost as xgb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report,accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import joblib
import nltk
import re
from nltk.stem import WordNetLemmatizer
from Modelling.utils import remove_stopwords

# Load the datasets (train, test, validation)
train_df = pd.read_excel("../db/train_data.xlsx")
test_df = pd.read_excel("../db/test_data.xlsx")
val_df = pd.read_excel("../db/validation_data.xlsx")

train_df["Notes"] = train_df["Notes"].apply(remove_stopwords)
test_df["Notes"] = test_df["Notes"].apply(remove_stopwords)
val_df["Notes"] = val_df["Notes"].apply(remove_stopwords)

# Replace class labels in the DataFrame
mapping = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}

train_df['Class'] = train_df['Class'].map(mapping)
test_df['Class'] = test_df['Class'].map(mapping)
val_df['Class'] = val_df['Class'].map(mapping)

X_train, y_train = train_df['Notes'], train_df['Class']
X_test, y_test = test_df['Notes'], test_df['Class']

from catboost import CatBoostClassifier, Pool
model = CatBoostClassifier(iterations=100, depth=6, learning_rate=0.1, loss_function='MultiClass')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Generate a classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

feature_importance = model.get_feature_importance()
print("Feature Importance:\n", feature_importance)



