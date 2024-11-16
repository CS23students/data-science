import numpy as np

nparray = np.array([[4, 5, 7], [2, 3, 1], [5, 9, 7], [9, 10, 15]])
testArr = np.array([2, 3, 1])
print("Original numpy Array: ", nparray)
print("Searched Array: ", testArr)
print("Index of searched array in the original array: ")
print(np.where((nparray == testArr).all(1))[0])
