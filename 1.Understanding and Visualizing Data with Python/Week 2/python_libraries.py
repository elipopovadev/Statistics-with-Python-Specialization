import numpy as np
import pandas as pd
from scipy import stats
from pylab import *
import matplotlib.pyplot as plt
import seaborn as sns


'''
NumPy

NumPy is the fundamental package for scientific computing with Python. It contains among other things:

    a powerful N-dimensional array object
    sophisticated (broadcasting) functions
    tools for integrating C/C++ and Fortran code
    useful linear algebra, Fourier transform, and random number capabilities

We will focus on the numpy array object.
Numpy Array

A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension.
'''

a = np.array([1, 2, 3])
print(a)
# Print object type
print(type(a))

# Print shape
print(a.shape)

# Print some values in a
print(a[0], a[1], a[2])

# Create a 2x2 numpy array
b = np.array([[1, 2], [3, 4]])
print(b)

# Print shape
print(b.shape)

# Create a 3x2 numpy array
c = np.array([[1, 2], [3, 4], [5, 6]])

# Print shape
print(c.shape)  # (3, 2)

# Print some values in c
print(c[0, 1], c[1, 0], c[2, 0], c[2, 1])

# 2x3 zero array
d = np.zeros((2, 3))

print(d)

# 4x2 array of ones
e = np.ones((4, 2))

print(e)

# 2x2 constant array
f = np.full((2, 2), 9)

print(f)

# 3x3 random array
g = np.random.random((3, 3))

print(g)

# Create 3x4 array
h = np.array([[1, 2, 3, 4, ], [5, 6, 7, 8], [9, 10, 11, 12]])

print(h)

# Slice array to make a 2x2 sub-array
i = h[0:2, 1:3]
print(i)
print(h)

# Modify the slice
i[0, 0] = 1738
print(h)
# Print to show how modifying the slice also changes the base object
print(h[0, 1])


# Integer
j = np.array([1, 2])
print(j.dtype)

# Float
k = np.array([1.0, 2.0])
print(k.dtype)

# Force Data Type
l = np.array([1.0, 2.0], dtype=np.int64)
print(l.dtype)

# Array Math
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

# Compute sum of all elements; prints "10"
x = np.array([[1, 2], [3, 4]])
print(np.sum(x))

# Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=0))

# Compute sum of each row; prints "[3 7]"
print(np.sum(x, axis=1))

# Compute mean of all elements; prints "2.5"
x = np.array([[1, 2], [3, 4]])
print(np.mean(x))

# Compute mean of each column; prints "[2 3]"
print(np.mean(x, axis=0))

# Compute mean of each row; prints "[1.5 3.5]"
print(np.mean(x, axis=1))


'''
SciPy

Numpy provides a high-performance multidimensional array and basic tools to compute with and manipulate these arrays. SciPy builds on this, and provides a large number of functions that operate on numpy arrays and are useful for different types of scientific and engineering applications.

For this course, we will primariyl be using the SciPy.Stats sub-library.
SciPy.Stats

The SciPy.Stats module contains a large number of probability distributions as well as a growing library of statistical functions such as:

    Continuous and Discrete Distributions (i.e Normal, Uniform, Binomial, etc.)

    Descriptive Statistcs

    Statistical Tests (i.e T-Test)
'''

# Print Normal Random Variables
print(stats.norm.rvs(size=10))


# Create some test data
dx = .01
X = np.arange(-2, 2, dx)
Y = exp(-X**2)

# Normalize the data to a proper PDF
Y /= (dx*Y).sum()

# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
plot(X, Y)
plot(X, CY, 'r--')
show()

# Compute the Normal CDF of certain values.
print(stats.norm.cdf(np.array([1, -1., 0, 1, 3, 4, -2, 6])))


'''
Descriptive Statistics
'''

np.random.seed(282629734)
# Generate 1000 Student’s T continuous random variables.
x = stats.t.rvs(10, size=1000)

# Do some descriptive statistics
print(x.min())   # equivalent to np.min(x)

print(x.max())   # equivalent to np.max(x)

print(x.mean())  # equivalent to np.mean(x)

print(x.var())   # equivalent to np.var(x))

stats.describe(x)


'''
MatPlotLib

Matplotlib is a plotting library. In this section give a brief introduction to the matplotlib.pyplot module.
'''

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  # You must call plt.show() to make graphics appear.

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

# Subplots
# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()

'''
Seaborn

Seaborn is complimentary to Matplotlib and it specifically targets statistical data visualization. But it goes even further than that: Seaborn extends Matplotlib and makes generating visualizations convenient.

While Matplotlib is a robust solution for various problems, Seaborn utilizes more concise paramesters for ease-of-use.
'''

# Scatterplots

# Store the url string that hosts our .csv file
url = "C:/Users/eli/Desktop/YtT9NroBEemddAqBQMk_og_f682394f0a2542cea617efa59089ab2b_Cartwheeldata.csv"

# Read the .csv file and store it as a pandas Data Frame
df = pd.read_csv(url)

# Create Scatterplot
sns.lmplot(x='Wingspan', y='CWDistance', data=df)

plt.show()

# Scatterplot arguments
sns.lmplot(x='Wingspan', y='CWDistance', data=df,
           fit_reg=False,  # No regression line
           hue='Gender')   # Color by evolution stage

plt.show()

# Construct Cartwheel distance plot
sns.swarmplot(x="Gender", y="CWDistance", data=df)

plt.show()

sns.boxplot(
    data=df.loc[:, ["Age", "Height", "Wingspan", "CWDistance", "Score"]])

plt.show()

# Male Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'M', [
            "Age", "Height", "Wingspan", "CWDistance", "Score"]])

plt.show()

# Female Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'F', [
            "Age", "Height", "Wingspan", "CWDistance", "Score"]])

plt.show()

# Male Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'M', ["Score"]])

plt.show()

# Female Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'F', ["Score"]])

plt.show()

# Distribution Plot (a.k.a. Histogram)
sns.distplot(df.CWDistance)

plt.show()

# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Gender', data=df)

plt.xticks(rotation=-45)

plt.show()
