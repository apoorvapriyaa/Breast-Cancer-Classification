import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from input import get_user_input

# Load breast cancer dataset
data = load_breast_cancer()

# Create a DataFrame from the dataset
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2,
                                                    random_state=42)

# Create a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate accuracy score
acc = accuracy_score(y_test, y_pred)

# Create the Streamlit app
st.title('Breast Cancer Classifier')
st.markdown('Is the Breast Cancer Malignant or Benign?')

# Add a sidebar for user input
st.sidebar.title('Breast Cancer Classifier')
st.sidebar.header('User Input')

# Get user input
user_input = get_user_input()

# Show the user input
st.subheader('Input Details:')
st.write(user_input)

# Make predictions on the user input
prediction = clf.predict(user_input)

# Show the prediction
st.subheader('Prediction:')
if prediction[0] == 0:
    st.write('The Breast Cancer is Malignant')
else:
    st.write('The Breast Cancer is Benign')

# Show the accuracy score
st.subheader('Accuracy:')
st.write(acc)
