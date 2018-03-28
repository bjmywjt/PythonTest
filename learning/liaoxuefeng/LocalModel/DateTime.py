from _datetime import datetime, timedelta


# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(1988, 4, 12, 5, 35, 0)
print(dt)

# timestamp\datetime互转
dt = datetime(1988, 4, 12, 5, 35, 0)
dts = dt.timestamp()
print(dts)
print(datetime.fromtimestamp(dts))

# str/datetime互转
str = '1988-04-12 05:36:00'
cday = datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
print(cday)
nowstr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nowstr)

# datetime加减
now = datetime.now()
print(now + timedelta(hours=5))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))