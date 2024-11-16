import numpy as np

arr1 = ['Java', 'C', 'C++']
arr2 = ['Python', 'Data', 'Science']
print("Original Arrays: ")
print(arr1, arr2)
result = np.r_[arr1[:-1], [arr1[-1]+arr2[0]], arr2[1:]]
print("\nAfter Combining: ")
print(result)
