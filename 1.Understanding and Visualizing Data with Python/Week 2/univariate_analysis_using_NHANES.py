import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

da = pd.read_csv(
    "C:/Users/eli/Desktop/YtPruboBEemdqA7UJJ_tgg_63e179e3722f4ef783f58ff6e395feb7_nhanes_2015_2016.csv")

''' Question 1
Relabel the marital status variable DMDMARTL to have brief but informative character labels.
Then construct a frequency table of these values for all people, then for women only, and for men only.
Then construct these three frequency tables using only people whose age is between 30 and 40. '''

da["DMDMARTL"] = da.DMDMARTL.replace({1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "Never married",
                                      6: "Living with partner",
                                      77: "Refused", 99: "Don't know"})

da["DMDMARTL"].value_counts()  # for all people

da_group_by_gender = da.groupby(["RIAGENDR"])
da_group_by_gender.get_group(2)["DMDMARTL"].value_counts()  # for all women
da_group_by_gender.get_group(1)["DMDMARTL"].value_counts()  # for all men

da[(da["RIDAGEYR"] >= 30) & (da["RIDAGEYR"] <= 40) & (da["RIAGENDR"] == 2)
   ].DMDMARTL.value_counts()  # for women with age between 30 and 40
da[(da["RIDAGEYR"] >= 30) & (da["RIDAGEYR"] <= 40) & (da["RIAGENDR"] == 1)
   ].DMDMARTL.value_counts()  # for men with age between 30 and 40


''' Q1a. Briefly comment on some of the differences that you observe between the distribution of marital status
 between women and men, for people of all ages. '''

# More men are separated than the women (118 vs 68)
# More women are widowed than the men (296 vs 100)
# More women are divorced than the men (350 vs 229)
# More men are married than the women (1477 vs 1303)

''' Q1b. Briefly comment on the differences that you observe between the distribution of marital status states for women
between the overall population, and for women between the ages of 30 and 40. '''
# The married women between overall population are 4 times more than the married women between 30 and 40. (1303 vs 285)
# The widowed women are about 15 times more than the widowed women between 30 and 40. ( 296 vs 2 )
# The women living with partner between overall population are more than the women living with partner between 30 and 40.

''' Q1c. Repeat part b for the men. '''
# Widowed men between 30 and 40 are less than the widowed men between overall population.
# The men never married between 30 and 40 are less than widowed men between overall population.
# Only one man between 30 and 40 refused to say about his marital status.


''' Question 2 
Restricting to the female population, stratify the subjects into age bands no wider than ten years,
and construct the distribution of marital status within each age band. Within each age band,
present the distribution in terms of proportions that must sum to 1. '''
da_only_women = da[da["RIAGENDR"] == 2]
da_only_women["agegrp"] = pd.cut(da_only_women.RIDAGEYR, [
                                 10, 20, 30, 40, 50, 60, 70, 80])
df = da_only_women.groupby("agegrp")["DMDMARTL"].value_counts(
    normalize=True, ascending=False)
print(df)


''' Q2a. Comment on the trends that you see in this series of marginal distributions. '''
# With age the number of "never married" women are decreasing.
# With age the number of "widowed" and "separated" women are increasing.

''' Q2b. Repeat the construction for males. '''
da_only_men = da[da["RIAGENDR"] == 1]
da_only_men["agegrp"] = pd.cut(da_only_men.RIDAGEYR, [
    10, 20, 30, 40, 50, 60, 70, 80])
df = da_only_men.groupby("agegrp")["DMDMARTL"].value_counts(
    normalize=True, ascending=False)
print(df)

''' Q2c. Comment on any notable differences that you see when comparing these results for females and for males. '''
# For this group [10,20] - 0.25 from the men is living with partner, but only 0,075 from the women is
# living with partner
# For those groups [10,20] and [20,30] there are not any widowed men. For this group [20-30] there are
# some widoewed women.


''' Question 3
Construct a histogram of the distribution of heights using the BMXHT variable in the NHANES sample. '''
sns.histplot(data=da, x='BMXHT', color='red',
             edgecolor='blue', linewidth=4, kde=False)


''' Q3a. Use the bins argument to distplot to produce histograms with different numbers of bins.
Assess whether the default value for this argument gives a meaningful result,
and comment on what happens as the number of bins grows excessively large or excessively small. '''
sns.histplot(data=da, x='BMXHT', color='red', bins=10,
             edgecolor='blue', linewidth=4, kde=False)
sns.histplot(data=da, x='BMXHT', color='red', bins=70,
             edgecolor='blue', linewidth=4, kde=False)
# When bins are excessively small it is difficult to see the count of different values and how data is spread.
# With too many bins the result is meaningless.

''' Q3b. Make separate histograms for the heights of women and men, then make a side-by-side boxplot
showing the heights of women and men. '''
da_only_men = da[da["RIAGENDR"] == 1]
da_only_women = da[da["RIAGENDR"] == 2]
sns.histplot(data=da_only_men, x='BMXHT', color='red',
             edgecolor='blue', linewidth=4, kde=False)
sns.histplot(data=da_only_women, x='BMXHT', color='red',
             edgecolor='blue', linewidth=4, kde=False)

DF = pd.DataFrame(
    {'bmxht_men': da_only_men['BMXHT'].dropna(), 'bmxht_women': da_only_women['BMXHT'].dropna()})
ax = DF[['bmxht_men', 'bmxht_women']].plot(
    kind='box', title='Diff between men and women', showmeans=True)
plt.show()

''' Q3c. Comment on what features, if any are not represented clearly in the boxplots, and what features, 
if any, are easier to see in the boxplots than in the histograms. '''
# In the boxplots we can't see how data is distributed, but we can see the median, Q1, Q3 and all outliers.


''' Question 4
Make a boxplot showing the distribution of within-subject differences between the first and second systolic blood pressure
measurents (BPXSY1 and BPXSY2). '''
da["BPXSYDIF"] = (da.BPXSY1-da.BPXSY2)
sns.boxplot(x=da["BPXSYDIF"].dropna())

''' Q4a. What proportion of the subjects have a lower SBP on the second reading compared to the first? '''
mean_bpxsy1 = da["BPXSY1"].mean()
mean_bpxsy2 = da["BPXSY2"].mean()
diff = mean_bpxsy1 - mean_bpxsy2
print(diff)  # 0.30159679687274377


''' Q4b. Make side-by-side boxplots of the two systolic blood pressure variables.'''
bp = sns.boxplot(data=da.loc[:, ["BPXSY1", "BPXSY2"]])

''' Q4c. Comment on the variation within either the first or second systolic blood pressure measurements,
and the variation in the within-subject differences between the first and second systolic blood pressure measurements. '''
da["BPXSYDIF"].dropna().describe()
# The First sistolic blood pressure measurements have higher median than the second blood pressure measurements, but
# but not drastically higher. The second systolic blood pressure measurements have more outliers.
# 50% have diff between BPXSY1 and BPXSY2 above and bellow 0.67 mm/Hg (the median).
# The bottom 25% have diff bellow -2(Q1), which means higher BPXSY2.
# The top 25% (Q3) have diff higher than 4 mm/Hg.
# Min diff is -26 mm/Hg and max diff is 32 mm/Hg.

''' Question 5
Construct a frequency table of household sizes for people within each educational attainment category
(the relevant variable is DMDEDUC2). Convert the frequencies to proportions. '''
da["DMDEDUC2"] = da.DMDEDUC2.replace({1: "Less than 9th grade", 2: "9-11th grade (Includes 12th grade with no diploma)",
                                      3: "High school graduate/GED or equivalent", 4: "Some college or AA degree",
                                      5: "College graduate or above",
                                      7: "Refused", 9: "Don't know"})
da["DMDEDUC2"] = da["DMDEDUC2"].dropna()
da.groupby("DMDEDUC2")["DMDHHSIZ"].value_counts(normalize=True)

''' Q5a. Comment on any major differences among the distributions. '''
# The group with less than 9th grade is the group with highest household from 7 "DMDHHSIZ"-
# 0.129771 compared to the others groups.
# The group "Don't know" is the group with the highest proportion with household from 2 (0.666667).


''' Q5b. Restrict the sample to people between 30 and 40 years of age. 
Then calculate the median household size for women and men within each level of educational attainment. '''
da_only_men = da[(da["RIAGENDR"] == 1) & (
    da["RIDAGEYR"] >= 30) & (da["RIDAGEYR"] <= 40)]
da_only_women = da[(da["RIAGENDR"] == 2) & (
    da["RIDAGEYR"] >= 30) & (da["RIDAGEYR"] <= 40)]
da_only_men.groupby("DMDEDUC2")["DMDHHSIZ"].median()
da_only_women.groupby("DMDEDUC2")["DMDHHSIZ"].median()

''' Question 6
The participants can be clustered into "maked variance units" (MVU) based on every combination of the variables SDMVSTRA
and SDMVPSU. Calculate the mean age (RIDAGEYR), height (BMXHT), and BMI (BMXBMI) for each gender (RIAGENDR),
within each MVU, and report the ratio between the largest and smallest mean (e.g. for height) across the MVUs. '''
da['MVU'] = da.groupby(['SDMVSTRA', 'SDMVPSU']).grouper.group_info[0]
da_men = da[(da["RIAGENDR"] == 1)]
da_women = da[(da["RIAGENDR"] == 2)]

df_men = da_men.groupby(["MVU"])["RIDAGEYR", "BMXHT",
                                 "BMXBMI"].mean()  # mean for men
df_women = da_women.groupby(
    ["MVU"])["RIDAGEYR", "BMXHT", "BMXBMI"].mean()  # mean for women

# report the ratio between the largest and smallest mean
df_men["RIDAGEYR"].max() / df_men["RIDAGEYR"].min()
df_women["RIDAGEYR"].max() / df_women["RIDAGEYR"].min()

df_men["BMXHT"].max() / df_men["BMXHT"].min()
df_women["BMXHT"].max() / df_women["BMXHT"].min()

df_men["BMXBMI"].max() / df_men["BMXBMI"].min()
df_women["BMXBMI"].max() / df_women["BMXBMI"].min()

''' Q6a. Comment on the extent to which mean age, height, and BMI vary among the MVUs.'''
# The mean age vary the most among the MVU, because the diff between the smallest and the largest value is the largest (13.09 for women and  13,10 for men)

''' Q6b. Calculate the inter-quartile range (IQR) for age, height, and BMI for each gender and each MVU.
 Report the ratio between the largest and smalles IQR across the MVUs. '''
df_men["RIDAGEYR"].describe()  # IQR = 50,70 - 45,36
df_women["RIDAGEYR"].describe()  # IQR = 50,89 - 44,51

df_men["BMXHT"].describe()
df_women["BMXHT"].describe()

df_men["BMXBMI"].describe()
df_women["BMXBMI"].describe()
