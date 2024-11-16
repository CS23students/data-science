import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anu', 'Sree', 'Mahesh', 'Karthik', 'Suriya'],
    'score': [12.4, 9, 16, 5, np.nan],
    'attempts': [1, 3, 2, 3, 2],
    'quality': ['yes', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(exam_data, index=labels)
print("Rows where score is missing: ")
print(df[df['score'].isnull()])
