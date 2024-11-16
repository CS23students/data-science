import pandas as pd
df1 = pd.DataFrame({
    'w': [68, 75, 56, 80, None],
    'x': [78, 85, None, 80, 86],
    'y': [84, 94, 89, 83, 86],
    'z': [86, 97, 96, 72, 83]
})

df2 = pd.DataFrame({
    'w': [78, 75, 86, 80, None],
    'x': [78, 85, 96, 80, 76],
    'y': [84, 84, 89, 83, 86],
    'z': [86, 97, 96, 72, 83]
})

print("Original Dataframes: ")
print(df1)
print(df2)
print("\nCheck for inequality of the solid Dataframe")
print(df1 != df2)
