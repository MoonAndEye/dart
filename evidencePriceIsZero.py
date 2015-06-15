# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 09:21:10 2015

"""
# to evidence what if we encounter 0 in start price

import os, random

def csvToArray(day_array, encode_setting):
    def_array = []
    with open(day_array, encoding = str(encode_setting)) as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
    return def_array


history_list = []

for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)

totalNum = int(len(history_list))

d0 = totalNum - 1
d1 = totalNum - 2
d2 = totalNum - 3


d0_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d0], 'shift-jis')
d1_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d1], 'shift-jis')

#print (d0_array[87])
#print (type(d0_array[62][5]),type(d0_array[66][6]))


a = '-'
array_num = int(len(d0_array))
array_num = array_num - 1000

#如果要在家裡使用這段，記得!!要把range從0開始設定.
for i in range(2,array_num):
    if d0_array[i][9] == '0':
        print (d0_array[i][0])

#資料不明者, 64, 66, 71, 82, 84, 87. 93
#for i in range(60,70):
#    print (d0_array[i])
