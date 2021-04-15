#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:23:29 2021

@author: nicole
"""

def listToString(numericalList):
    result = ""
    
    #transform the numerical list into a string
    for l in numericalList:
        result += str(l)
        
    return result

def encodeHash(input_hash):
    #turns hash into an array
    list_char = list(input_hash)
    
    converted_char = []

    for c in list_char:
        #transform the character to int and add to the list
        converted_char.append(int(c, base=16))
        
    return listToString(converted_char)

import pandas as pd

def encodeHashList(hash_list, col, target):
    #transform the col into a list
    hashes = hash_list[col].to_list()
    #transform the col target into a list
    col_target = hash_list[target].to_list()
        
    for i in range(0, len(hashes)):
        #transform the values in the col into numerical hashes
        hashes[i] = encodeHash(hashes[i])
        
    #transform back into a dataframe
    dataframe_data = { col: hashes, target: col_target }
    return pd.DataFrame(data=dataframe_data)