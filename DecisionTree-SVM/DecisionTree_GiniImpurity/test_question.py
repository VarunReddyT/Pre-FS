'''
Exercise 1: Implementing Decision Trees with Gini Impurity

Description:
In this exercise, you will explore the concept of Gini Impurity and its role in creating decision trees. 

The tasks include:
1. Calculating Gini Impurity for datasets.
2. Splitting the dataset and evaluating Gini Gain for various splits.
3. Identifying the best feature and threshold for a split based on maximum Gini Gain.

Dataset Overview:
The dataset consists of three features: dosage, age, and gender, and one label: effectiveness of the drug. 

Explanation of features in the dataset:
| Feature       | Description                                                  | Data Type   | Example Values  |
|---------------|--------------------------------------------------------------|-------------|-----------------|
| dosage        | Dosage level of the drug (in mg)                             | Numeric     | 10, 20, 30      |
| age           | Age of the patient (in years)                                | Numeric     | 25, 35, 45      |
| gender        | Gender of the patient (encoded: 0 = male, 1 = female)        | Categorical | 0, 1            |
| effectiveness | Effectiveness of the drug (0 = not effective, 1 = effective) | Binary      | 0, 1            |

***Important Instructions***
1. Fill in the missing code to complete this assignment. Missing code is indicated as "# your code here".
2. "DecisionTreeClassifierGini" class with boiler plate code is pre-defined for you, the missing logic must be implemented correctly.
3. The "main" method must run and generate output in the format specified in the code, this is important as test cases invoke the main method for evaluation.
'''

import numpy as np
import pandas as pd

class DecisionTreeClassifierGini:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def gini_impurity(self, y):
        # your code here
        return gini_impurity_val

    def split(self, X_column, threshold):
        # your code here
        return left_indices, right_indices

    def calculate_gini_split(self, y, left_indices, right_indices):
        # your code here
        return gini

    def find_best_split(self, X, y):
        # your code here
        return best_feature, best_threshold, best_gini

    def build_tree(self, X, y, depth=0):
        if len(np.unique(y)) == 1 or (self.max_depth is not None and depth >= self.max_depth):
            return np.argmax(np.bincount(y))

        feature, threshold, gini = self.find_best_split(X, y)
        if feature is None:
            return np.argmax(np.bincount(y))

        left_indices, right_indices = self.split(X[:, feature], threshold)
        left_subtree = self.build_tree(X[left_indices], y[left_indices], depth + 1)
        right_subtree = self.build_tree(X[right_indices], y[right_indices], depth + 1)

        return {
            "feature": feature,
            "threshold": threshold,
            "left": left_subtree,
            "right": right_subtree
        }

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def predict_sample(self, x, tree):
        if isinstance(tree, dict):
            feature = tree["feature"]
            threshold = tree["threshold"]
            if x[feature] <= threshold:
                return self.predict_sample(x, tree["left"])
            else:
                return self.predict_sample(x, tree["right"])
        return tree

    def predict(self, X):
        return np.array([self.predict_sample(x, self.tree) for x in X])


# Function to take user input and make predictions
def main():
    # Accept user input for new data
    print("Provide new data (dosage, age, gender) below:")
    new_data = []
    
    '''
    # Collect dosage, age, gender (1 record for prediction)
    # Your input in the terminal should look like
    Provide new data (dosage, age, gender) below:
    10
    25
    0
    '''
    dosage = float(input())
    age = float(input())
    gender = int(input())
    new_data.append([dosage, age, gender])
        
    new_data = np.array(new_data)

    # Example dataset for training
    data = {
        "dosage": [10, 20, 10, 30, 40, 50, 60, 20, 30, 40],
        "age": [25, 35, 45, 20, 30, 50, 60, 40, 28, 22],
        "gender": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        "effectiveness": [0, 1, 0, 1, 1, 1, 0, 1, 1, 0]
    }

    df = pd.DataFrame(data)
    X = df[["dosage", "age", "gender"]].values
    y = df["effectiveness"].values

    # Train decision tree classifier
    clf = DecisionTreeClassifierGini(max_depth=5)
    clf.fit(X, y)

    # Predict on user input data
    predictions = clf.predict(new_data)
    prediction = predictions[0]
    return prediction


output = main()
print(output)

    
    
    
 
    