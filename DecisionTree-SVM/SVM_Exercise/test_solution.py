'''
Exercise 1: Implement SVM from scratch using Numpy, Pandas

Description:
In this exercise, you will implement a basic Support Vector Machine (SVM) model from scratch using only NumPy and Pandas libraries. The goal is to classify a synthetic dataset into two categories: Non-diabetic and Diabetic.

You are required to:
1. Implement a linear SVM model that:
   - Uses a hyperplane to classify the data samples.
   - Updates weights and bias using gradient descent during training.
2. Test the model by predicting the class of a new data sample.

Dataset overview:
| Feature      | Description                                                                           |
|--------------|---------------------------------------------------------------------------------------|
| Glucose      | Represents the glucose level of a patient. Higher values indicate potential diabetes. |
| BMI          | Body Mass Index, a measure of body fat based on weight and height.                    |
| Age          | Age of the patient, contributing to diabetes risk assessment.                         |
| Label        | Binary classification: `0` for Non-diabetic, `1` for Diabetic.                        |

The dataset contains 200 samples, with 100 samples each for Non-diabetic and Diabetic classes. The features are generated synthetically using random sampling, with distinct means for each class to ensure separability.

***Important Instructions***
1. Fill in the missing code to complete this assignment. Missing code is indicated as "# your code here".
2. Boiler plate code is pre-defined for you, the missing logic must be implemented correctly.
3. The "main" method must run and generate output in the format specified in the code, this is important as test cases invoke the main method for evaluation.
'''

import numpy as np
import pandas as pd

# NOTE: This is programmatically generated sample dataset, it does not follow the standard ranges of the features (Glucose, BMI, Age).
# Generate a synthetic diabetes dataset
def generate_diabetes_data():
    np.random.seed(42)
    # Generate data for two classes: Non-diabetic and Diabetic
    non_diabetic = np.random.multivariate_normal(mean=[2, 2, 2], cov=np.eye(3), size=100)
    diabetic = np.random.multivariate_normal(mean=[6, 6, 6], cov=np.eye(3), size=100)

    # Create labels: 0 for non-diabetic, 1 for diabetic
    non_diabetic_labels = np.zeros(non_diabetic.shape[0])
    diabetic_labels = np.ones(diabetic.shape[0])

    # Combine the data and labels
    data = np.vstack((non_diabetic, diabetic))
    labels = np.hstack((non_diabetic_labels, diabetic_labels))

    return pd.DataFrame(data, columns=['Glucose', 'BMI', 'Age']), pd.Series(labels, name='Label')

# Implement a basic linear SVM model
def train_svm(X, y, learning_rate=0.01, epochs=1000, lambda_param=0.01):
    n_samples, n_features = X.shape

    # Initialize weights and bias
    weights = np.zeros(n_features)
    bias = 0

    for epoch in range(epochs):
        for idx, x_i in enumerate(X):
            condition = y[idx] * (np.dot(x_i, weights) - bias) >= 1
            if condition:
                # If correctly classified, update weights and bias without penalty
                weights -= learning_rate * (2 * lambda_param * weights)
            else:
                # Misclassified sample, update with penalty
                weights -= learning_rate * (2 * lambda_param * weights - np.dot(x_i, y[idx]))
                bias -= learning_rate * y[idx]
                
    return weights, bias

# Make predictions
def predict(X, weights, bias):
    pred = np.sign(np.dot(X, weights) - bias)
    return pred

def main():
    # Init dataset, labels and train the SVM
    # Generate the diabetes dataset
    data, labels = generate_diabetes_data()

    # Convert labels to -1 and 1 for SVM
    labels = labels.apply(lambda x: -1 if x == 0 else 1)

    # Train the SVM
    X = data.values
    y = labels.values
    weights, bias = train_svm(X, y)

    # Take new sample data from user for prediction
    print("Provide new data (Glucose, BMI, Age) below:")
    new_data = []
    
    '''
    # Collect Glucose, BMI, Age (1 record for prediction)
    # Your input in the terminal should look like
    Provide new data (Glucose, BMI, Age) below:
    5.5
    4.0
    3.0
    '''
    glucose = float(input())
    bmi = float(input())
    age = float(input())
    new_data.append([glucose, bmi, age])
    sample = np.array(new_data)

    # Predict using SVM
    prediction = predict(sample.reshape(1, -1), weights, bias)
    class_label = "Diabetic" if prediction == 1 else "Non-diabetic"
    return class_label

output = main()
print(output)


