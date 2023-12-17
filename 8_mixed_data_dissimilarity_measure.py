# عدم تشابه داده های ترکیبی

import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from gower import gower_matrix

# Sample mixed data
data = np.array([
    [25, 'Male', 150, 'High'],
    [30, 'Female', 130, 'Medium'],
    [35, 'Male', 160, 'Low'],
    [28, 'Female', 140, 'Medium'],
    [40, 'Male', 170, 'High']
])

# Separate numeric and categorical columns
# ستون های داده های اسمی و عددی
numeric_columns = [0, 2]
categorical_columns = [1]

# Create a ColumnTransformer to apply different preprocessing to numeric and categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_columns),
        ('cat', OneHotEncoder(), categorical_columns)
    ]
)

# Create a pipeline with preprocessing and Gower distance calculation
pipeline = Pipeline([
    ('preprocessor', preprocessor),
])

# Fit the pipeline and transform the data
transformed_data = pipeline.fit_transform(data)

# Calculate Gower distance matrix
gower_dist_matrix = gower_matrix(transformed_data)

# Display the Gower distance matrix
print("Gower Distance Matrix:")
print(gower_dist_matrix)
