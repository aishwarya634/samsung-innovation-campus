import pandas as pd
import numpy as np
import datetime
from datetime import date, datetime,time,timezone
datetime(2025,12,5,15,50)


d=date(2025,12,5)
t=time(13,26,10)
print(datetime.combine(d,t))
print(datetime.now())
print(datetime.now(timezone.utc))
print(datetime.now().date())
print(datetime.now().time())
print(pd.Timestamp("2025,12,01"))

my_birth=datetime(1973,7,7)
today=datetime.today()
tommorrow=today+pd.Timedelta(days=1)
print(tommorrow-my_birth)











90
