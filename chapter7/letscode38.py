import pandas as pd 
import numpy as np
import datetime
import matplotlib.pyplot as plt 
from datetime import date,datetime,time,timezone
df = pd.read_csv("./chapter8/Month_Value_1.csv")
print(df.head())
print()
print(df.tail())
df.info()
df.isnull().sum()
change_value=0
df=df.fillna(change_value)
df.isnull().sum()
df['Period']=pd.to_datetime(df['Period'])
df.set_index('Period',inplace=True)
print(df.head())
print()
print(df.tail())
df.info()
plt.style.use('ggplot')
cols=['Revenue','Average_cost']
df[cols].plot(kind='area',alpha=0.2,stacked=False,figsize=(20,10))
plt.xlabel('Period')
plt.ylabel('Value')
plt.legend()
plt.show()
x=df.index
y1=df['Revenue']
y2=df['Sales_quantity']
y3=df['Average_cost']
fig,axs=plt.subplots(1,3,figsize=(18,5))
axs[0].plot(x,y1,color='blue')
axs[0].set_title('Revenue Over Time')
axs[0].set_xlabel('Period')
axs[0].set_ylabel('Revenue')
axs[1].plot(x,y1,color='green')
axs[1].set_title('Sales Quantity Over Time')
axs[1].set_xlabel('Period')
axs[1].set_ylabel('Sales Quantity')
axs[2].plot(x,y1,color='red')
axs[2].set_title('Average Cost Over Time')
axs[2].set_xlabel('Period')
axs[2].set_ylabel('Average Cost')


fig.suptitle('Monthly Performance Trends', fontsize=16)
plt.tight_layout()
plt.show()