# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:45:38 2016

@author: g3094510
"""
import os

def csvToArray(day_array, encode_setting):
    def_array = []
    with open(day_array, encoding = str(encode_setting)) as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
    return def_array
    
    
def sortDataFromNew (source_list, index):
    #source_list,是目標的list,第二個是存放目標的diction名字,第三個是裡面的code
    history_number = int(len(source_list)) - 1   
    code = str(index)
    def_diction = {}
    for i in range(history_number):
        def_diction[code + str(i)] = source_list[history_number]
        history_number = history_number - 1
    return def_diction
