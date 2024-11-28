import numpy as np

# Creating an array and reshaping it to 5 dimensions (1 element per dimension in this example)
array = np.array([2, 3, 4, 5, 6]).reshape(1, 1, 1, 1, 5)

print("Array shape: ", array.shape)                 # Outputs the shape of the array
print("Number of dimensions: ", array.ndim)         # Prints the number of dimensions
print(array)


# OUTPUT:
# Array shape:  (1, 1, 1, 1, 5)
# Number of dimensions:  5
# [[[[[2 3 4 5 6]]]]]
