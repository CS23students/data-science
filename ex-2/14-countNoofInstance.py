import numpy as np

x = np.array([15, -15, 15, 20, 15, -15])
y = np.array([1, 2, 3, 4, 5, 6])
print("Original Array: ")
print(x)
print(y)
result = np.sum((x == 15) & (y > 0))
print("\nNumber of instance of value occur in one array on condition of another array: ")
print(result)
