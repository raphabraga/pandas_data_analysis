import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df = pd.read_excel("./dataset/AdventureWorks.xlsx")

print(df.shape)