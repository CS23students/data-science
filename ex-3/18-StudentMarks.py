import pandas as pd
data = {
    'studentId': [201, 202, 203, 204, 205],
    'name': ['ALice', 'Bob', 'Charlie', 'Stuart', 'Eve'],
    'maths': [80, 90, 78, 92, 88],
    'science': [87, 92, 75, 95, 83],
    'history': [84, 88, 90, 92, 79]
}

df = pd.DataFrame(data)
print(df)
