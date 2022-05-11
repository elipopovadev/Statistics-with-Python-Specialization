import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv(
    "C:/Users/eli/Desktop/YtPruboBEemdqA7UJJ_tgg_63e179e3722f4ef783f58ff6e395feb7_nhanes_2015_2016.csv")

df.head()

# get columns names
col_names = df.columns
col_names

# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
        'BMXWAIST']
keep = [column for column in col_names if 'BMX' in column]
df_BMX = df[keep]
df_BMX.head()

#  column indexing
# .loc is primarily label based, but may also be used with a boolean array.
# .iloc is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.
df.loc[:, keep].head()
index_bool = np.isin(df.columns, keep)
index_bool
df.iloc[:, index_bool].head()  # Indexing with boolean list

# Selection by conditions
# Lets only look at rows who 'BMXWAIST' is larger than the median
# get the median of 'BMXWAIST'
waist_median = pd.Series.median(df_BMX['BMXWAIST'])
waist_median
df_BMX[df_BMX['BMXWAIST'] > waist_median].head()
# Lets add another condition, that 'BMXLEG' must be less than 32
condition1 = df_BMX['BMXWAIST'] > waist_median
condition2 = df_BMX['BMXLEG'] < 32
df_BMX[condition1 & condition2].head()  # Using [] method
# Note: can't use 'and' instead of '&'

df_BMX.loc[condition1 & condition2, :].head()  # Using df.loc[] method
# note that the conditiona are describing the rows to keep

# Lets make a small dataframe and give it a new index so can more clearly see the differences between .loc and .iloc
tmp = df_BMX.loc[condition1 & condition2, :].head()
# If you use different years than 2015-2016, this my give an error. Why?
tmp.index = ['a', 'b', 'c', 'd', 'e']
tmp
tmp.loc[['a', 'b'], 'BMXLEG']
tmp.iloc[[0, 1], 3]
