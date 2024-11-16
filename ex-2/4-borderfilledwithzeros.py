import numpy as np

arr = np.array([[1, 2, 3], [4, 8, 1], [3, 7, 9]])
print("Original Array: ", arr)
print("0 on the border around existing array")
arr = np.pad(arr, pad_width=1, mode="constant", constant_values=0)
print(arr)
