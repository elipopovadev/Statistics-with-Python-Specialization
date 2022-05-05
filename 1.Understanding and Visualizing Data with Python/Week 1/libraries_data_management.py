import numpy as np
import pandas as pd

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.mean(a))  # 5.0

# Importing Data
# Store the url string that hosts our .csv file (note that this is a different url than in the video)
url = "C:/Users/eli/Desktop/YtT9NroBEemddAqBQMk_og_f682394f0a2542cea617efa59089ab2b_Cartwheeldata.csv"

# Read the .csv file and store it as a pandas Data Frame
df = pd.read_csv(url)

# Output object type
print(type(df))  # <class 'pandas.core.frame.DataFrame'>

# We can view our Data Frame by calling the head() function
df.head()

# Index(['ID', 'Age', 'Gender', 'GenderGroup', 'Glasses', 'GlassesGroup',
print(df.columns)
# 'Height', 'Wingspan', 'CWDistance', 'Complete', 'CompleteGroup',
# 'Score'],
# dtype='object')


# Return all observations of CWDistance
df.loc[:, "CWDistance"]

# Select all rows for multiple columns, ["CWDistance", "Height", "Wingspan"]
df.loc[:, ["CWDistance", "Height", "Wingspan"]]

# Select few rows for multiple columns, ["CWDistance", "Height", "Wingspan"]
df.loc[:9, ["CWDistance", "Height", "Wingspan"]]

# Select range of rows for all columns
df.loc[10:15]

# Now, let's say we only want to return the first 10 observations:
df.loc[:9, "CWDistance"]


'''
 .iloc()

.iloc() is integer based slicing, whereas .loc() used labels/column names.
'''
df.iloc[:4]
df.iloc[1:5, 2:4]

df.dtypes

# List unique values in the df['Gender'] column
df.Gender.unique()

# Use .loc() to specify a list of mulitple column names
df.loc[:, ["Gender", "GenderGroup"]]

# From eyeballing the output, it seems to check out. We can streamline this by utilizing the groupby() and size() functions.
df.groupby(['Gender', 'GenderGroup']).size()
