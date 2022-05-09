import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import numpy as np


# First, you must import the data
df = pd.read_csv(
    "C:/Users/eli/Desktop/YtPruboBEemdqA7UJJ_tgg_63e179e3722f4ef783f58ff6e395feb7_nhanes_2015_2016.csv")

# Next, look at the 'head' of our DataFrame 'df'.
df.head(2)

# Lets only consider the feature (or variable) 'BPXSY2'
bp = df['BPXSY2']
print(bp)

# What is the mean of 'BPXSY2'?
bp_mean = np.mean(bp)
print(bp_mean)  # 124.78301716350497

# Are the excluded entirely? Are they counted as zeros? Something else? If you used a library function,
# try looking up the documentation using the code:
help(np.mean)  # None

# To make sure we know that we aren't treating missing data in ways we don't want,
# lets go ahead and drop all the nans from our Series 'bp'
bp = bp.dropna()

# Find the: Median, Max, Min, Standard deviation, Variance
print(np.min(bp))  # min = 84.0
print(np.max(bp))  # max = 238.0
print(np.std(bp))  # std = 18.525338021233832
print(np.var(bp))  # variance = 343.1881488009719
print(np.median(bp))  # median = 122.0
print(np.mean(bp))  # mean = 124.78301716350497

# Using the fact that 'bp' is a pd.Series object, can use the pd.Series method diff()
# call this method by: pd.Series.diff()
diff_by_series_method = bp.diff()
# note that this returns a pd.Series object, that is, it had an index associated with it
# only want to see the values, not the index and values
print(diff_by_series_method.values)

# Now use the numpy library instead to find the same values
# np.diff(array)
diff_by_np_method = np.diff(bp)
diff_by_np_method  # array([ 16.,  -8.,   2., ...,  30., -40.,   8.])
# note that this returns an 'numpy.ndarray', which has no index associated with it, and therefore ignores
# the nan we get by the Series method

# We could also implement this ourselves with some looping
diff_by_me = []  # create an empty list
for i in range(len(bp.values)-1):  # iterate through the index values of bp
    # find the difference between an element and the previous element
    diff = bp.values[i+1] - bp.values[i]
    diff_by_me.append(diff)  # append to out list
np.array(diff_by_me)  # format as an np.array

# How to find the interquartile range
bp_iqr = stats.iqr(bp)
print(bp_iqr)  # 22.0

# Visualizing the data
# use the Series.describe() method to see some descriptive statistics of our Series 'bp'
bp.describe()  # median = 122.000000, min = 84.000000, std = 18.527012

# Make a histogram of our 'bp' data using the seaborn library we imported as 'sns'
sns.set(style='darkgrid')
sns.histplot(data=bp, x=bp, linewidth=1, edgecolor='black').set(
    title='BPXSY2 vs Count')

# # Make a boxplot of our 'bp' data using the seaborn library. Make sure it has a title and labels!
sns.set(style='darkgrid')
sns.boxplot(data=bp, x=bp, linewidth=1).set(title='BPXSY2 vs Count')
