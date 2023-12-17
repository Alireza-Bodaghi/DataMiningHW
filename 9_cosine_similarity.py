import numpy as np
from numpy.linalg import norm
# تشابه کسینوسی
def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    norm1 = norm(vector1)
    norm2 = norm(vector2)
    
    similarity = dot_product / (norm1 * norm2)
    return similarity

vector1 = [1, 2, 3, 4, 5]
vector2 = [2, 4, 6, 8, 10]

similarity = cosine_similarity(vector1, vector2)

print("Cosine Similarity : ", similarity)
