import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data set
tips_data = sns.load_dataset("tips")

# Print out the first few rows of the data
print(tips_data.head())

# Print out the summary statistics for the quantitative variables
tips_data.describe()

# Plot a histogram of the total bill
sns.histplot(data=tips_data, x='total_bill',
             color='red', linewidth=2, edgecolor='black', kde=True)
plt.title('Histogram of total bill')

# Plot a histogram of the Tips only
sns.histplot(data=tips_data, x='tip',
             color='blue', kde=True)
plt.title('Histogram of tips')

# Plot a histogram of both the total bill and the tips'
sns.distplot(tips_data['tip'], kde=False, label='Tip')
sns.distplot(tips_data['total_bill'], kde=False, label='Total bill')
plt.legend(prop={'size': 12})
plt.xlabel('Tip and Total bill')


# Create a boxplot of the total bill amounts
sns.boxplot(x='total_bill', data=tips_data, linewidth=3)

# Create a boxplot of the tips amounts
sns.boxplot(x='tip', data=tips_data, linewidth=3)

# Create a boxplot of the tips and total bill amounts
col1 = tips_data['tip']
col2 = tips_data['total_bill']
DF = pd.DataFrame({'tip': col1, 'total_bill': col2})
ax = DF[['tip', 'total_bill']].plot(
    kind='box', title='boxplot', showmeans=True)
plt.show()

# Create a boxplot and histogram of the tips grouped by smoking status
smoking_groups = tips_data.groupby(['smoker'])
smoking_no = smoking_groups.get_group('No')
smoking_yes = smoking_groups.get_group('Yes')

col1 = smoking_no['tip']
col2 = smoking_yes['tip']
DF = pd.DataFrame({'tip_no_smoking': col1, 'tip_smoking': col2})
ax = DF[['tip_no_smoking', 'tip_smoking']].plot(
    kind='box', title='boxplot', showmeans=True)
plt.show()

sns.distplot(smoking_no['tip'], label='Tips for non-smokers')
sns.distplot(smoking_yes['tip'], label='Tips for smokers')
plt.legend(prop={'size': 12})
plt.xlabel('Tip for non-smokers and smokers')

# Create a boxplot and histogram of the tips grouped by time of day
time_groups = tips_data.groupby(['time'])
lunch_time = time_groups.get_group('Lunch')
dinner_time = time_groups.get_group('Dinner')

col1 = lunch_time['tip']
col2 = dinner_time['tip']
DF = pd.DataFrame({'lunch_time': col1, 'dinner_time': col2})
ax = DF[['lunch_time', 'dinner_time']].plot(
    kind='box', title='boxplot', showmeans=True)
plt.show()

sns.distplot(lunch_time['tip'], label='Tips for lunch_time')
sns.distplot(dinner_time['tip'], label='Tips for dinner_time')
plt.legend(prop={'size': 12})
plt.xlabel('Tips for lunch_time and  dinner_time')

# Create a boxplot and histogram of the tips grouped by the day
time_groups = tips_data.groupby(['day'])
sun_time = time_groups.get_group('Sun')
sat_time = time_groups.get_group('Sat')
thur_time = time_groups.get_group('Thur')
fri_time = time_groups.get_group('Fri')

col1 = sun_time['tip']
col2 = sat_time['tip']
col3 = thur_time['tip']
col4 = fri_time['tip']
DF = pd.DataFrame({'sunday': col1, 'saturday': col2,
                  'thursday': col3, 'friday': col4})
ax = DF[['sunday', 'saturday', 'thursday', 'friday']].plot(
    kind='box', title='boxplot', showmeans=True)
plt.show()

g = sns.FacetGrid(tips_data, row='day')
g = g.map(plt.hist, 'tip')
