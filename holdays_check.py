# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:45:56 2016

@author: Moon
"""

from holidays_jp import CountryHolidays


def holidaysList(year):
    """
    input 4 digit in year
    """
    holidays = CountryHolidays.get('JP',int(year))
    
    return_list = []
    
    for i in holidays:
        return_list.append(i[0].strftime("%Y-%m-%d"))
    return(return_list)

"""below is test
    
x = holidaysList(2016)

print(x)
"""