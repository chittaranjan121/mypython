import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv("C:\\Users\\Adish\\Downloads\\bank.csv")
sns.lineplot(x='day',y='duration',data=df,hue='month',ci=True,style='month',markers=True)
plt.show()