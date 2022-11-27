import calendar
def Day_Name(d,m,y):
    day = calendar.day_name[calendar.weekday(y,m,d)]
    print(day.upper())
Day_Name(7,1,2021)