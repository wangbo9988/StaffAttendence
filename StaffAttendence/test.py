import datetime

date = datetime.datetime.now()
print(date.strftime('%Y-%m-%d %H:%M:%S')[0:10])
print((date+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')[0:10])
