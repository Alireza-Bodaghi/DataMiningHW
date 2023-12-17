import pandas as pd
from scipy.spatial.distance import pdist, squareform

# عدم تشابه داده های اسمی
# Sample data
data = {
    'Animal': ['Cat', 'Dog', 'Bird', 'Fish', 'Horse'],
    'Color': ['Brown', 'Black', 'Yellow', 'Silver', 'Brown']
}

df = pd.DataFrame(data)

# Create a dissimilarity matrix
dissimilarity_matrix = pdist(pd.get_dummies(df['Color']))

# Convert the dissimilarity matrix to a square matrix
square_matrix = squareform(dissimilarity_matrix)

# Convert to DataFrame for better visualization
dissimilarity_df = pd.DataFrame(
    square_matrix, 
    index=df['Animal'], 
    columns=df['Animal']
)

print("Dissimilarity Matrix:")
print(dissimilarity_df)
