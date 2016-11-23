from datetime import datetime,timedelta

#获取当前时间
now  = datetime.now()
print(now)
print(type(now))

#设置指定时间
dt = datetime(2016,4,22,12,24)
print(dt)

#datetime转timestamp
#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
print(dt.timestamp())

#timestamp转换为datetime
dt_timestamp = dt.timestamp()

print(dt.fromtimestamp(dt_timestamp))

#timestamp也可以直接被转换到UTC标准时区的时间
print(dt.utcfromtimestamp(dt_timestamp))

#datetime转换为str
print(now.strftime('%a,%b %d %H:%M'))


from datetime import timedelta
#datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2,hours=12))


#本地时间转换为UTC时间
from datetime import timezone
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
timestr= '2015-1-21 9:01:30'
date=datetime.strptime(timestr,"%Y-%m-%d %H:%M:%S")  #字符串转datetime
utc_userZone = timezone(timedelta(hours=5))  #设置指定的timezone对象
print(utc_userZone)
userZoneTime = date.replace(tzinfo=utc_userZone) #直接修改指定时间在指定时区的时间
print(userZoneTime.timestamp()) #datetiime转换成timestamp













