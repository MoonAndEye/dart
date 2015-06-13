# -*- coding: utf-8 -*-

"""
Created on Fri Jun 12 11:45:30 2015

"""
import os, random


display_list = []
history_list = []
# d0 表示的是當天的股價, d1是前1天,d2是前2天
d0_array = []
d1_array = []

def csvToArray(day_array):
    def_array = []
    with open(day_array, encoding = 'shift-jis') as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
        return def_array
        
#d0_array = csvToArray('C:/1save/jpStock/raw/2015-06-10.csv')



for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)
    
history_number = int(len(history_list))
d0 = history_number -1
d1 = history_number -2
d2 = history_number -3
d3 = history_number -4
d4 = history_number -5


print (history_list[d0])
print (history_list[d1])
#print (history_list[4])
date_d0 = history_list[d0][:-4]
date_d1 = history_list[d1][:-4]
print (date_d0)
print (date_d1)


d0_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d0])
d1_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d1])
#print (d0_array[2])

dart_array = []

for i in range(5): 
    dart0 = random.choice(d0_array)
    dart_array.append(dart0)
    #print (dart0[0])

#with open('C:/1save/jpStock/dart/test.csv', 'xt', encoding = 'shift-jis') as f:
#    for i in range(5):
#        f.write(str(dart_array[i]).replace('\'', '')[1:-1] + '\n\r')
        
#for i in range(0,5):
#    print ("d" + str(i) +"=" +  str(random.randint(0,2000))


#for i in range(5):
#        print (str(dart_array[i]).replace('\'', '')[1:-1])