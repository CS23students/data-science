import numpy as np

nparray = np.array([[10, 5, 8], [17, 2, 2]])
print("Original Array: ")
print(nparray)
print("Type: ", type(nparray))
print("Sequence: 1,2")
result = repr(nparray).count("2")
result2 = repr(nparray).count("10")
print("Number of occurences: ")
print(result, result2)
