# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:28:00 2015

"""

import os
import numpy

def csvToArray(day_array):
    def_array = []
    with open(day_array, encoding = 'shift-jis') as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
        return def_array


dart_name_list = [] #此list放的是之前抽選的結果

for name in os.listdir('C:/1save/jpStock/dart'):
    dart_name_list.append(name)

dart_target = int(len(dart_name_list)) - 3 
# 上面這個現在是減3，真的在算的時候可能是減2，不能減1，減1是detail

# print (dart_name_list) 
# print (dart_name_list[dart_target])
dart_d1 = [] #dart_d1 是前一天的飛標結果，是個list，裡面存放5個飛標加日期

dart_d1 = csvToArray('C:/1save/jpStock/dart/' + str(dart_name_list[dart_target]))
for i in range(1,6):
    dart_d1.pop(i)
#目前不知道為什麼 dar_d1裡面，每個飛標後面都會出現一個空 list。只好手動消掉他。
#未來一定要找一下為什麼，可能問題在 飛標原始檔 ，不然就是寫入list那邊
dart_d1.append(str(dart_name_list[dart_target]))
#加入日期在 dart_d1[5]，如果以後要debug，可以直接呼叫

for i in range(0,5):
    print (dart_d1[i][0])

history_list = []

for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)

#以下是把d0和歷史資料的位置抓出來，預測是d1，所以算損益要  d1 = d0 +1
d0index = history_list.index(str(dart_name_list[dart_target])[:-4] + '.csv')
print (d0index)
d1index = int(d0index + 1)
print (d1index)
print (history_list[d1index]) #這就是目標

d1_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d1index])
#d1_array 是歷史資料的array

benefit_array = []
a = int(len(d1_array))
print (a)



for code in range(a):
    if d1_array[code][0] == '4558-T':
        print (code)
        benefit_array.append(d1_array[code])    

print (benefit_array)

    
"""
with open ('C:/1save/jpStock/dart/detail/detail.txt', 'at', encoding = 'shift-jis') as f:
    f.write ('test')
"""