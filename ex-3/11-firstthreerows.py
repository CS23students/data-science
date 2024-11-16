import pandas as pd
import numpy as np

exam_data = {
    'name': ['Jane', 'Dime', 'John', 'Heena', 'Raja'], 'some': [12.5, 9, 16.5, np.nan, 8], 'attempts': [1, 3, 2, 3, 2],
    'quality': ['yes', 'no', 'yes', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(exam_data, index=labels)
print("First three rows of the Dataframe: ")
print(df[:3])
