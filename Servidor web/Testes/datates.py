
from datetime import datetime
from datetime import timedelta

data = "06/01/1980 00:00"
data = datetime.strptime(data, '%d/%m/%Y %H:%M')
datahj = datetime.now()
first_day = data - timedelta(days=data.isoweekday())
first_dayy = data - timedelta(days=datahj.isoweekday())
print(data)

data = first_dayy - timedelta()
print(data)