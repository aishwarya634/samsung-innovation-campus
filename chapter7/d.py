import matplotlib.pyplot as plt
import pandas_datareader as pdr
df=pdr.get_data_fred('GS10')
print(df.info())
print(df.describe())
plt.plot(df)
plt.show()