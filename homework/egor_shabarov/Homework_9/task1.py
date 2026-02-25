import datetime

date_str = 'Jan 15, 2023 - 12:05:33'

date_py = datetime.datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')

print(datetime.datetime.strftime(date_py, '%B'))
print(datetime.datetime.strftime(date_py, '%d.%m.%Y, %H:%M'))
