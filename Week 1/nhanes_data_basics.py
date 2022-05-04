import pandas as pd

url = "C:/Users/eli/Desktop/YtPruboBEemdqA7UJJ_tgg_63e179e3722f4ef783f58ff6e395feb7_nhanes_2015_2016.csv"
da = pd.read_csv(url)

da.shape  # (5735, 28)

da.columns
''' Index(['SEQN', 'ALQ101', 'ALQ110', 'ALQ130', 'SMQ020', 'RIAGENDR', 'RIDAGEYR',
       'RIDRETH1', 'DMDCITZN', 'DMDEDUC2', 'DMDMARTL', 'DMDHHSIZ', 'WTINT2YR',
       'SDMVPSU', 'SDMVSTRA', 'INDFMPIR', 'BPXSY1', 'BPXDI1', 'BPXSY2',
       'BPXDI2', 'BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
       'BMXWAIST', 'HIQ210'],
        dtype='object') '''

da.dtypes

w = da["DMDEDUC2"]
print(w)
x = da.loc[:, "DMDEDUC2"]
print(x)
y = da.DMDEDUC2
z = da.iloc[:, 9]  # DMDEDUC2 is in column 9

''' Another reason to slice a variable out of a data frame is so that we can then pass it into a function.
 For example, we can find the maximum value over all DMDEDUC2 values using any one of the following four lines of code: '''

print(da["DMDEDUC2"].max())
print(da.loc[:, "DMDEDUC2"].max())
print(da.DMDEDUC2.max())
print(da.iloc[:, 9].max())

print(type(da))  # The type of the variable; <class 'pandas.core.frame.DataFrame'>
# The type of one column of the data frame; <class 'pandas.core.series.Series'>
print(type(da.DMDEDUC2))
# The type of one row of the data frame; <class 'pandas.core.series.Series'>
print(type(da.iloc[2, :]))

x = da.iloc[3:5, :]
y = da.iloc[:, 2:5]


# Missing values
print(pd.isnull(da.DMDEDUC2).sum())
print(pd.notnull(da.DMDEDUC2).sum())
