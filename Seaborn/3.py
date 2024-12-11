

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
x1=[1,2,3,4]
y1=[4,5,6,7]
df=pd.DataFrame({"A":x1,"B":y1})
sns.lineplot(x=x1,y=y1,data=df,marker=True)
plt.show()
