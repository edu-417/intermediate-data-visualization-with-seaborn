import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

grant_file = "../datasets/schoolimprovement2010grants.csv"
df = pd.read_csv(grant_file)

sns.displot(df["Award_Amount"], bins=20)
# plt.show()

sns.displot(df["Award_Amount"], kind="kde", rug=True, fill=True)
plt.show()