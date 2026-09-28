import pandas as pd
special_day=pd.Period("1973-7",freq="M")
special_day
pd.Period()
print(special_day.start_time)
print(special_day.end_time)
pd.Period()
n=special_day+2
print(special_day)
print(n)
n.start_time,n.end_time

