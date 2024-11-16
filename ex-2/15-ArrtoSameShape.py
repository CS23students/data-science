import numpy as np

arr1 = np.random.random(size=(1, 1, 1))
arr2 = np.random.random(size=(1, 1, 1))
arr3 = np.random.random(size=(1, 1, 1))
print("Original Array: ", arr1, arr2, arr3)
result = np.concatenate((arr1, arr2, arr3), axis=-1)
print("\nAfter Concatenation: ")
print(result)
