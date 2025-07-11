import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Load dataset
df = pd.read_csv('dataset/train_u6lujuX_CVtuZ9i.csv')

# Clean & filter data
df = df[['ApplicantIncome', 'LoanAmount', 'Credit_History', 'Loan_Status']].dropna()

# Rename columns
df.rename(columns={
    'ApplicantIncome': 'Income',
    'LoanAmount': 'LoanAmount',
    'Credit_History': 'CreditScore',
    'Loan_Status': 'Label'
}, inplace=True)

# Convert 'Loan_Status' to numeric
df['Label'] = df['Label'].map({'Y': 1, 'N': 0})

# Add synthetic Age (since not in dataset)
np.random.seed(42)
df['Age'] = np.random.randint(21, 60, size=len(df))

# Define features and label
X = df[['Age', 'Income', 'CreditScore', 'LoanAmount']]
y = df['Label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained with 4 features and saved as model.pkl")
