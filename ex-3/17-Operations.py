import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)
new_row = pd.DataFrame({'name': ['invalid'], 'age': [28]})
df = pd.concat([df, new_row], ignore_index=True)
sliced_df = df[1:3]
data2 = {'name': ['Eve', 'Front'], 'age': [22, 40]}
df2 = pd.DataFrame(data2)

combined = pd.concat([df, df2])
print(combined)
