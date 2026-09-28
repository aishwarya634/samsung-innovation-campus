import pandas as pd
wti = pd.read_csv("./chapter8/DCOILWTICO.csv")
print(wti.head())
print()
print(wti.tail())
print(wti.info())
wti['N_DATE'] = pd.to_datetime(wti['observation_date'])

print(wti.head())
print(wti.info())
df=wti.drop(['observation_date'],axis=1)
print(df.info())
df = df.set_index("N_DATE")
print(df['2025-11-04':'2025-11-10'])