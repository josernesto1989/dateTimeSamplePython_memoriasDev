import datetime

now = datetime.datetime.now()

for x in range(10):
    currentDate = now + datetime.timedelta(days=0+x)
    print(str(currentDate.year)+'-'+str(currentDate.month)+'-'+str(currentDate.day))