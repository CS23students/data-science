import numpy as np

arr = np.array([1, 2, 3, 4])

print("Options: \n1. Insert \n2. Search \n3.Sort\n4. Delete\n5. Exit")
ch = 0
while (ch != 5):
    ch = int(input("Enter choice: "))
    if (ch == 1):
        print("Array before insertion: ", arr)
        el = int(input("Enter element to insert: "))
        pos = int(input("Enter position: "))
        arr = np.insert(arr, pos, el)
        print("Array after insertion: ", arr)
    elif (ch == 2):
        searchel = int(input("Enter element to be search: "))
        pos = np.where(arr == searchel)[0]
        print("Position: ", pos)
    elif (ch == 3):
        print("Sorted array: ", np.sort(arr))
    elif (ch == 4):
        delEl = int(input("Enter position of the element to be deleted: "))
        arr = np.delete(arr, delEl)
        print("Array after deletion: ", arr)
    elif (ch == 5):
        print("EXIT...")
    else:
        print("Invalid choice")
