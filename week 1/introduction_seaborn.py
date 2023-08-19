import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import matplotlib
# matplotlib.use("qtagg")

grant_file = "../datasets/schoolimprovement2010grants.csv"
df = pd.read_csv(grant_file)

df["Award_Amount"].plot.hist()
plt.show()

plt.clf()

#Display a Seaborn displot
sns.displot(df["Award_Amount"])
plt.show()

plt.clf()