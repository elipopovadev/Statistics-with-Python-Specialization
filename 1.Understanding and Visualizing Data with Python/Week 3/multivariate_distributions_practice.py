import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

da = pd.read_csv(
    "C:/Users/eli/Desktop/YtPruboBEemdqA7UJJ_tgg_63e179e3722f4ef783f58ff6e395feb7_nhanes_2015_2016.csv")

'''
Question 1
Make a scatterplot showing the relationship between the first and second measurements of diastolic blood pressure (BPXDI1 and BPXDI2). 
Also obtain the 4x4 matrix of correlation coefficients among the first two systolic and the first two diastolic blood pressure measures.
'''
sns.scatterplot(data=da, x="BPXDI1", y="BPXDI2",  alpha=0.3)
# Most of the data is concentrated between 40 and 100 BPXDI1 and between 40 and 100 BPXDI2

df = da.loc[:1, ["BPXDI1", "BPXDI2"]]
df.corr()
'''      BPXDI1  BPXDI2
BPXDI1     1.0     1.0
BPXDI2     1.0     1.0 '''


'''
Question 2
Construct a grid of scatterplots between the first systolic and the first diastolic blood pressure measurement.
Stratify the plots by gender (rows) and by race/ethnicity groups (columns).
'''
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
sns.FacetGrid(da, row="RIAGENDR",  col="RIDRETH1").map(
    plt.scatter, "BPXDI1", "BPXDI2", alpha=0.4).add_legend()


'''
Question 3

Use "violin plots" to compare the distributions of ages within groups defined by gender and educational attainment.
'''
sns.FacetGrid(da, row="RIAGENDR", col="DMDEDUC2").map(
    sns.violinplot, "RIDAGEYR", alpha=0.4).add_legend()


'''
Question 4

Use violin plots to compare the distributions of BMI within a series of 10-year age bands. Also stratify these plots by gender.
'''
da["agegroup"] = pd.cut(da.RIDAGEYR, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

sns.FacetGrid(da, row="RIAGENDR", col="agegroup").map(
    sns.violinplot, "BMXBMI", alpha=0.4).add_legend()


'''
Question 5

Construct a frequency table for the joint distribution of ethnicity groups (RIDRETH1) and health-insurance status (HIQ210).
Normalize the results so that the values within each ethnic group are proportions that sum to 1.
'''
x = pd.crosstab(da.RIDRETH1, da.HIQ210)
x.apply(lambda z: z/z.sum(), axis=1)
