import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from imblearn.over_sampling import SMOTE

# Load dataset
data = pd.read_csv('creditcard.csv')

print("First few rows:")
print(data.head())

# Check class distribution
print("\nClass distribution:")
print(data['Class'].value_counts())

# Plot class distribution
sns.countplot(x='Class', data=data)
plt.title('Class Distribution')
plt.show()

# Separate features and target
X = data.drop('Class', axis=1)
y = data['Class']

# Apply SMOTE to balance dataset
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

print("\nAfter SMOTE, class distribution:")
print(pd.Series(y_res).value_counts())

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.3, random_state=42, stratify=y_res)

# Define Logistic Regression model and parameter grid (reduced for memory)
lr = LogisticRegression(max_iter=1000, random_state=42)
lr_params = {'C': [0.1, 1]}  # smaller grid

# Define Random Forest model and parameter grid (reduced for memory)
rf = RandomForestClassifier(random_state=42)
rf_params = {'n_estimators': [50], 'max_depth': [10]}

# GridSearchCV with n_jobs=1 to avoid memory errors
lr_grid = GridSearchCV(lr, lr_params, cv=3, scoring='f1', n_jobs=1)
rf_grid = GridSearchCV(rf, rf_params, cv=3, scoring='f1', n_jobs=1)

# Fit Logistic Regression grid search
print("\nFitting Logistic Regression GridSearchCV...")
lr_grid.fit(X_train, y_train)
print("Best params LR:", lr_grid.best_params_)

# Predict and evaluate Logistic Regression
y_pred_lr = lr_grid.predict(X_test)
print("\nLogistic Regression Classification Report:")
print(classification_report(y_test, y_pred_lr))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_lr))

# Fit Random Forest grid search
print("\nFitting Random Forest GridSearchCV...")
rf_grid.fit(X_train, y_train)
print("Best params RF:", rf_grid.best_params_)

# Predict and evaluate Random Forest
y_pred_rf = rf_grid.predict(X_test)
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

# Plot confusion matrices
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

sns.heatmap(confusion_matrix(y_test, y_pred_lr), annot=True, fmt='d', ax=ax[0], cmap='Blues')
ax[0].set_title('Logistic Regression Confusion Matrix')
ax[0].set_xlabel('Predicted')
ax[0].set_ylabel('Actual')

sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt='d', ax=ax[1], cmap='Greens')
ax[1].set_title('Random Forest Confusion Matrix')
ax[1].set_xlabel('Predicted')
ax[1].set_ylabel('Actual')

plt.show()
