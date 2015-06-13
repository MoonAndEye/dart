# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:28:00 2015

"""

import os

def csvToArray(day_array):
    def_array = []
    with open(day_array, encoding = 'shift-jis') as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
        return def_array


dart_result_list = [] #此list放的是之前抽選的結果

for name in os.listdir('C:/1save/jpStock/dart'):
    dart_result_list.append(name)

dart_target = int(len(dart_result_list)) - 3 
# 上面這個現在是減3，真的在算的時候可能是減2，不能減1，減1是detail

# print (dart_result_list) 
# print (dart_result_list[dart_target])

d1_array = csvToArray('C:/1save/jpStock/dart/' + str(dart_result_list[dart_target]))
print (d1_array[0])

"""
with open ('C:/1save/jpStock/dart/detail/detail.txt', 'at', encoding = 'shift-jis') as f:
    f.write ('test')
"""