"""
Created on Fri Jun 12 11:45:30 2015

"""
import os
import random

display_list = []
history_list = []
# d0 表示的是當天的股價, d1是前1天,d2是前2天
d0_array = []
d1_array = []
d2_array = []
d3_array = []
d4_array = []

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


print (history_list[2])
print (history_list[3])
print (history_list[4])

d0_array = csvToArray('C:/1save/jpStock/raw/' + history_list[d0])
#print (d0_array[2])

dart_array = []

for i in range(5): #挑出d0_array 中
    dart1 = random.choice(d0_array)
    dart_array.append(dart1)
    #print (dart1)
    
    
for i in range(5):
    print (dart_array[i])
#for i in range(0,5):
#    print ("d" + str(i) +"=" +  str(random.randint(0,2000))
