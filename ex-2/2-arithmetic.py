import numpy as np

arr1 = np.array([1, 3, 4])
arr2 = np.array([8, 2, 3])

op = 'y'
print("Choices \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division\n5. Modulus\n6. Power")

while (op == 'y'):
    ch = int(input("Enter choice: "))
    if (ch == 1):
        add = np.add(arr1, arr2)
        print("Addition: ", add)
    elif (ch == 2):
        sub = np.subtract(arr1, arr2)
        print("Subtraction: ", sub)
    elif (ch == 3):
        mul = np.multiply(arr1, arr2)
        print("Multiplication : ", mul)
    elif (ch == 4):
        div = np.divide(arr1, arr2)
        print("Division: ", div)
    elif (ch == 5):
        rem = np.mod(arr1, arr2)
        print("Modulus: ", rem)
    elif (ch == 6):
        pow = np.power(arr1, arr2)
        print("Power: ", pow)
    else:
        print("Enter valid choice")
    op = input("Do you want to continue (y/n): ")
