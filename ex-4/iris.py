import pandas as pd
d = pd.read_csv(r"C:\Users\cse\Documents\Data science\ex-4\Irirs.csv")
print("The length of the dataset: ", len(d))
start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
print("After slicing: \n", d[start:stop])
n = int(input("Enter the specific row to display: "))

print(d.iloc[n])
print(d.describe())
E = input("Enter column name to be replaced: ")
G = input("Enter new name: ")
replace = {E: G}
d.rename(columns=replace, inplace=True)
print("Dataset:\n", d)
