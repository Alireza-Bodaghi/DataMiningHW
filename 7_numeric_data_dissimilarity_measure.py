import numpy as np
from sklearn.metrics import pairwise_distances

# عدم تشابه داده های عددی
# Sample data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
# فاصله اقلدسی 
# Calculate Euclidean distance using pairwise_distances
dissimilarity_matrix = pairwise_distances(
    data, 
    metric='euclidean'
)

# Display the dissimilarity matrix
print("Dissimilarity Matrix with euclidean:")
print(dissimilarity_matrix)
