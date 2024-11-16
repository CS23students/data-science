import numpy as np

fvalues = [10, 12, 43, 30, 90, 20]
F = np.array(fvalues)
cvalues = [-15.78, 15, 18, 35]
c = np.array(cvalues)
print("Values in fahrenheit: ", fvalues)
print("Values in celcius: ", cvalues)

print("Values in celcius degree: ")
print(np.round(((F-32)*5/9), 3))
print("Values in fahrenheit degree: ")
print(np.round((9*c/5+32), 2))
