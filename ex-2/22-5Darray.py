import numpy as np

array = np.random.rand(2, 3, 4, 5, 6)
num_dim = array.ndim
print("Array shape: ", array.shape)
print("Number of dimensions: ", num_dim)
print(array)
