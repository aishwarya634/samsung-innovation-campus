import pandas_datareader as pdr
from pandas_datareader import wb
import pandas as pd
all_indicators=pdr.wb.get_indicators()
print(all_indicators.iloc[:5,:2])

df1=pd.DataFrame({
    "aish":[34,45],"vicky":[78,56]
})
df2=pd.DataFrame({
    "aish":[56,45],"cat":[89,78]
})
s=pd.concat([df1,df2], ignore_index=True)
print(s)

s2 = pd.merge(df1, df2, on="aish")
print(s2)