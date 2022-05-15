import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1.First, you must import the cartwheel data from the path given above
df = pd.read_csv(
    "C:/Users/eli/Desktop/YtT9NroBEemddAqBQMk_og_f682394f0a2542cea617efa59089ab2b_Cartwheeldata.csv")

# 2.Next, look at the 'head' of our DataFrame 'df'
df.head()

# 3.Make a Seaborn scatter plot with x = height and y = wingspan using sns.scatterplot(x, y)
scater = sns.jointplot(x=df["Height"], y=df["Wingspan"], hue=df["Gender"])
df_no_nulls = df[["Height", "Wingspan"]].dropna()
pearsonr, p = stats.pearsonr(df_no_nulls.Height, df_no_nulls.Wingspan)
pearson_str = f'pearsonr = {pearsonr:.2f}; p = {p}'

scater.ax_joint.text(
    scater.ax_joint._axes.xaxis.get_data_interval()[1],
    scater.ax_joint._axes.yaxis.get_data_interval()[1],
    pearson_str,
    horizontalalignment='right')
plt.show()

# 4.Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance
sc = sns.jointplot(x=df["Wingspan"], y=df["CWDistance"])
df_no_nulls = df[["Wingspan", "CWDistance"]].dropna()
pearsonr, p = stats.pearsonr(df_no_nulls.Wingspan, df_no_nulls.CWDistance)
pearson_str = f'pearsonr = {pearsonr:.2f}; p = {p}'


sc.ax_joint.text(
    sc.ax_joint._axes.xaxis.get_data_interval()[1],
    sc.ax_joint._axes.yaxis.get_data_interval()[1],
    pearson_str,
    horizontalalignment='right')
plt.show()

# 5.Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance, and hue = gender
sns.scatterplot(data=df, x=df["Wingspan"],
                y=df["CWDistance"], hue=df["Gender"])

# 6.Make a Seaborn barplot with x = glasses and y = cartwheel distance
sns.set(style='darkgrid')
plt.figure(figsize=(10, 5), dpi=200)
sns.barplot(data=df, x="Glasses", y="CWDistance", estimator=np.mean, ci='sd')

# 7.Make the same Seaborn boxplot as above, but include gender for the hue argument
sns.set(style='darkgrid')
plt.figure(figsize=(10, 5), dpi=200)
sns.barplot(data=df, x="Glasses", y="CWDistance",
            estimator=np.mean, ci='sd', hue=df["Gender"])
