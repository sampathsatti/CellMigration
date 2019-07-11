import pandas as pd
from matplotlib import pyplot as pt
import seaborn as sns

# Read dataset
df = pd.read_csv('Pokemon.csv', index_col=0)

# Display first 5 observations
df.head()
sns.lmplot(x='Attack', y='Defense', data=df)
