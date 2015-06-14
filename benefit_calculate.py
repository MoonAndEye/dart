# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:28:00 2015

"""

import os
import numpy

def csvToArray(day_array, encode_setting):
    def_array = []
    with open(day_array, encoding = str(encode_setting)) as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
    return def_array

        

dart_name_list = [] #此list放的是之前抽選的txt結果

for name in os.listdir('C:/1save/jpStock/dart'):
    dart_name_list.append(name)

    

dart_target_date = int(len(dart_name_list)) - 3 
# 上面這個現在是減3，真的在算的時候可能是減2，不能減1，減1是detail

# print (dart_name_list) 
# print (dart_name_list[dart_target_date])
dart_d1 = [] #dart_d1 是前一天的飛標結果，是個list，裡面存放5個飛標加日期

dart_d1 = csvToArray('C:/1save/jpStock/dart/' + str(dart_name_list[dart_target_date]), 'utf-8')
for i in range(1,6):
    dart_d1.pop(i)
#目前不知道為什麼 dar_d1裡面，每個飛標後面都會出現一個空 list。只好手動消掉他。
#未來一定要找一下為什麼，可能問題在 飛標原始檔 ，不然就是寫入list那邊
dart_d1.append(str(dart_name_list[dart_target_date]))
#加入日期在 dart_d1[5]，如果以後要debug，可以直接呼叫


# for i in range(0,5):
    # print (dart_d1[i][0])
# 印出前一天射的飛標，只印code
    
history_list = []

for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)

#以下是把d0和歷史資料的位置抓出來，預測是d1，所以算損益要  d1 = d0 +1
d0index = history_list.index(str(dart_name_list[dart_target_date])[:-4] + '.csv')
# print (d0index)
d1index = int(d0index + 1)
# print (d1index)
# print (history_list[d1index]) #這就是目標

d1_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d0index], 'shift-jis')
#d1_array 是歷史資料的array

dart_result_array = []  #這個 list 放的是隔天射出來的飛標結果
a = int(len(d1_array))
# print (a)

dart_target = [] #這個list 放的是目標代碼，不是日期

for target in range(5):
    for code in range(a):
        if d1_array[code][0] == dart_d1[target][0]:
            # print (code) #印出所找到的index是不是真的在list中那個位置
            dart_result_array.append(d1_array[code])    

for i in range(5):
    print (dart_result_array[i]) #印出飛標的結果，是d0的始高安終

benefit_array = []
total_benefit = 0
for i in range(5):
    unit_benefit = float(dart_result_array[i][7]) - float(dart_result_array[i][4])
    holding_volumn = 1000000/int(dart_result_array[i][4])
    dart_unit_benefit = holding_volumn * unit_benefit
    total_benefit = total_benefit + dart_unit_benefit
    print ('The benefit of %s is %.0f' % (dart_result_array[i][0], dart_unit_benefit))
    # benefit_array[i].append((dart_result_array[0]))
#要存的目標[0],[1],[2],[3],[4],[7]
benefit_ratio = total_benefit / 50000

# print (type(benefit_ratio))
print ('Total benefit is %.0f jpy, and benefit persentage is %.2f percent' % (total_benefit, benefit_ratio))