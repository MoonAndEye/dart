# -*- coding: utf-8 -*-

"""
Created on Fri Jun 12 11:45:30 2015
"""
import os, random, time
start_time = time.time()
# os 是為了拿來找目錄下的檔案, random是為了射飛標, time是為了執行時間


# d0 表示的是當天的股價, d1是前1天,d2是前2天
d0_array = []
d1_array = []

def csvToArray(day_array, encode_setting):
    def_array = []
    with open(day_array, encoding = str(encode_setting)) as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
    return def_array
        
#d0_array = csvToArray('C:/1save/jpStock/raw/2015-06-10.csv')

#history_list 放的是歷史資料,裡面順序從遠排到近
history_list = []
for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)

#選擇要選個數,排序很花時間,一定要-1，因為array一直是從0開始算    
history_number = int(len(history_list))
d0 = history_number -1 #要射的飛標只要這個
d1 = history_number -2
d2 = history_number -3
d3 = history_number -4
d4 = history_number -5


#print (history_list[d0])
#print (history_list[d1])
#print (history_list[4])
date_d0 = history_list[d0][:-4]  #這是為了給後面的csv檔有日期
date_d1 = history_list[d1][:-4]
#print (date_d0)
#print (date_d1)

#下面是把射完的飛標的儲存位置變成字串
file_d0 = str('C:/1save/jpStock/dart/' + str(date_d0) + '.txt')
file_d1 = str('C:/1save/jpStock/dart/' + str(date_d1) + '.txt')
#print ('The darts results were saved in ' + str(file_d0))

#把d0內的資料轉成2d array,注意一定要用 shift-jis,否則編碼會錯誤
d0_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d0], 'shift-jis')
d1_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d1], 'shift-jis')
#print (d0_array[2])



#以下是最早的版本,但可能出現重復的選項,而且也可能出現不能交易的目標
"""
for i in range(5): 
    dart0 = random.choice(d0_array)
    dart_array.append(dart0)
    #print (dart0[0])
"""
#以下是新版本,用random.sample,可射中不會重復的目標,並存在dart_array

dart_array = []
dart0 = random.sample(d0_array, 5)
for i in range(5):
    dart_array.append(dart0[i])

#print (dart_array[0][9])

#這一段是為了找出交易量為0的飛標,若有,視為沒射中
for j in range(5):
    while dart_array[j][9] == '0': #這一行有問題,IndexError: list index out of range
    #如果沒抽中交易量為0,則沒問題. 若交易量為0, 則有 indexError,該用if-else嗎        
        print (str(dart_array[j][0]) + ' is 0, re-dart ')
        dart_array[j] = random.choice(d0_array) #這一行不能用random.sample,這指令會回傳list,造成indexError
        print ('the new target is ' + str(dart_array[j][0]))
    print (str(dart_array[j][0]) + ' is target')

#這是為確認今天是否抽過了,若已抽過, check 值為 True
check = os.path.isfile(file_d0)

if check == True:
    print ('You already shooted darts.\nThe new darts results won\'t come out.')
#若沒抽,則產生檔案,並把飛標結果寫入
else:
    with open(file_d0 , 'xt', encoding = 'utf-8') as f: #如果設定成 xt 表示如果檔案已經存在，則不寫入。測試時要改 at
        for i in range(5):
            f.write(str(dart_array[i]).replace('\'', '')[1:-1] + '\n\r')
    #這要回去看 benefitcalculate.py,此檔案的做用是把當日結果與累記算出,同時寫入detail    
    import benefit_calculate
    exec('benefit_calculate')#import完後,執行即可

print("Run time --- %s seconds ---" % (time.time() - start_time))
