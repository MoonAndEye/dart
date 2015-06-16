# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:28:00 2015
"""

import os
import time
start_time = time.time()
#import numpy

def csvToArray(day_array, encode_setting):
    def_array = []
    with open(day_array, encoding = str(encode_setting)) as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
    return def_array

        

dart_name_list = [] #此list放的是之前抽選的txt結果

for name in os.listdir('C:/1save/jpStock/dart'):
    dart_name_list.append(name)

    

dart_target_bef_date = int(len(dart_name_list)) - 3 
# 上面這個是標的日期,現在是減3，真的在算的時候可能是減2，不能減1，減1是detail

# print (dart_name_list) 
# print (dart_name_list[dart_target_bef_date])
dart_d1 = [] #dart_d1 是前一天的飛標結果，是個list，裡面存放5個飛標加日期

dart_d1 = csvToArray('C:/1save/jpStock/dart/' + str(dart_name_list[dart_target_bef_date]), 'utf-8')
for i in range(1,6):
    dart_d1.pop(i)
#目前不知道為什麼 dar_d1裡面，每個飛標後面都會出現一個空 list。只好手動消掉他。
#未來一定要找一下為什麼，可能問題在 飛標原始檔 ，不然就是寫入list那邊
dart_d1.append(str(dart_name_list[dart_target_bef_date]))
#加入日期在 dart_d1[5]，如果以後要debug，可以直接呼叫


# for i in range(0,5):
    # print (dart_d1[i][0])
# 印出前一天射的飛標，只印code
    
history_list = []

for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)

#以下是把d0和歷史資料的位置抓出來，預測是d1，所以算損益要  d1 = d0 +1
d0index = history_list.index(str(dart_name_list[dart_target_bef_date])[:-4] + '.csv')
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

dart_unit_benefit_array = []
benefit_array = []
total_benefit = 0
for i in range(5):
    unit_benefit = float(dart_result_array[i][7]) - float(dart_result_array[i][4])
    holding_volumn = 1000000/int(dart_result_array[i][4])
    dart_unit_benefit = holding_volumn * unit_benefit
    dart_unit_benefit_array.append(int(dart_unit_benefit))    
    total_benefit = total_benefit + dart_unit_benefit
    print ('The benefit of %s is %.0f' % (dart_result_array[i][0], dart_unit_benefit))
    # benefit_array[i].append((dart_result_array[0]))
#要存的目標[0],[1],[2],[3],[4],[7]
benefit_ratio = total_benefit / 50000

# print (type(benefit_ratio))
print ('Total benefit is %.0f jpy, and benefit persentage is %.2f percent' % (total_benefit, benefit_ratio))

#這邊放第每天結算的資料，如果出問題，則這邊回復
"""
revenue:4462
date:1
"""

d1_conclusion = []
#先讀取以前的資料，再做結算累加
file = open('C:/1save/jpStock/dart/detail/conclusion.txt', 'r', encoding = 'utf-8')

#因為我不確定怎麼讀完後刪除掉以前的資料
#所以先讀,抓出資料後,關閉,再開,再寫,再關閉(以後解決)
for line in file:
    d1_conclusion.append(line)
bef_revenue = str(d1_conclusion[0])[8:]
bef_date = str(d1_conclusion[1])[5:]
file.close()
#!!!注意, close()一定要加括號,不然關不起來,檔案會卡住

#bef表示前一天的資料,先讀進來,再獵今天的標的,再覆寫回去
print ('the bef_revenue is ' + bef_revenue)
print ('the bef_date is ' + bef_date)

aft_revenue = int(bef_revenue) + int(total_benefit)
aft_date = int(bef_date) + 1

#write_in1是第一行, revenue, write_in2是第二行,第幾次飛標
#因每支飛標以1M jpy計算,一天五支共5M,所以知道射幾次
#就可以算出獲利百分比 5M x date就是cost
write_in1 = 'revenue:'+str(aft_revenue)+'\n'
write_in2 = 'date:'+str(aft_date)

print ('the aft_revenue is ' + str(aft_revenue))
print ('the aft_date is ' + str(aft_date))

#先寫detail報告,再把下面這個打開
"""
file = open('C:/1save/jpStock/dart/detail/conclusion.txt', 'w', encoding = 'utf-8')
file.write(write_in1)
file.write(write_in2)
file.close()
"""

#下面開始寫detail_array, 裡面的金額都是 int 型別
#[0]date, [1]today_revenue, [2]acc_revenue, [3]duration, [4]dart1, [5]dart2, [6]dart3, [7]dart4, [8]dart5
detail_array = []
detail_array.append(str(name)[:-4]) 
detail_array.append(int(total_benefit)) #benefit 用於當天結算,revenue用統計
detail_array.append(aft_revenue)
detail_array.append(aft_date)
for i in range(5):
    detail_array.append(dart_unit_benefit_array[i])#不太對,我想要股票代號,名稱,和benefit
print(detail_array)

"""
detail_file = open('C:/1save/jpStock/dart/detail/detail.txt', 'a', encoding = 'utf-8')
detail_file.write(write_in1) #到時候把array放進去
detail_file.write(write_in2)
file.close()
"""


print("You sepnt --- %s seconds ---" % (time.time() - start_time))
