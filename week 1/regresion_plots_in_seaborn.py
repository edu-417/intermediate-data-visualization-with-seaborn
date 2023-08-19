import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../datasets/insurance_premiums.csv")

#Create a regresion plot
sns.regplot(data=df, x="insurance_losses", y="premiums")
# plt.show()

sns.lmplot(data=df, x="insurance_losses", y="premiums")
# plt.show()

#Plotting multiple variables
sns.lmplot(data=df, x="insurance_losses", y="premiums", hue="Region")
# plt.show()

#Facetting multiple regressions
sns.lmplot(data=df, x="insurance_losses", y="premiums", row="Region")
plt.show()