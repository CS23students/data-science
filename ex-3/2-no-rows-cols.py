# 2. A pandas program to count the number of rows and columns:



import pandas as pd
import numpy as np

exam_data={
  'name':['Abi','Vimal','kavi','ravi','sree'],
  'score':[12.5,19,16.5,np.nan,9],
  'attempts':[1,3,2,3,2],
  'quality':['yes','no','yes','no','no'],
}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
total_cols=len(df.axes[0])
total_rows=len(df.axes[1])
printf("No. of rows: ",str(total_rows))
printf("No. of cols: ",str(total_cols))


# Output:


# Number of rows: 4
# Number of columns: 5

