# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:45:56 2016

@author: Moon
"""

from holidays_jp import CountryHolidays
# get japanese holidays in 2015.
holidays = CountryHolidays.get('JP', 2016)

print(holidays[0][0])
a = holidays[0][0]

print(a.strftime("%Y-%m-%d"))

b = a.strftime("%Y")
print(b)

holidays_b = CountryHolidays.get('JP', int(b))
#print(holidays_b)

year_holidays = []
for i in holidays_b:
    foo = i[0]
    year_holidays.append(foo.strftime("%Y-%m-%d"))