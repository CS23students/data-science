import pandas as pd
df = pd.DataFrame({
    'name': ['Rahul', 'Erie', 'Ravi', 'Eesha', 'Vj', 'Moses'],
    'DateofBirth': ['17/05/2002', '16/02/2000', '25/09/1995', '11/05/2002', '15/09/2001', '01/01/1998'],
    'age': [18.5, 21.2, 22.5, 27, 23, 26]
})

print("Original Dataframe: ")
print(df)
label = pd.DataFrame(df['name'])
print("\nNumeric representation of an array by identifying distinct values: ")
print(label)
