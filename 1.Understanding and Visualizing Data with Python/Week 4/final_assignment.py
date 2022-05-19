import numpy as np  # for sampling for the distributions
import matplotlib.pyplot as plt  # for basic plotting
import seaborn as sns  # for plotting of the histograms

'''
1.
Question 1
In the code block below, generate 3 normal random variables with mean 100 and standard deviation 1. 
'''
mean = 100
sigma = 1

np.random.seed(123)
var1 = np.random.normal(mean, sigma)
var2 = np.random.normal(mean, sigma)
var3 = np.random.normal(mean, sigma)
print(var1, var2, var3)

'''
2.
Generating random samples from a population lies at the heart of statistics. In the code block below,
draw a sample of size 10 from a set containing the integers 1 through 100.
'''
size = 10
np.random.seed(123)
population = np.arange(1, 100)
sample = np.random.choice(population, size)
print(sample)
