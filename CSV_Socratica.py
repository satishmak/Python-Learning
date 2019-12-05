# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:25:26 2019

@author: Satish
https://www.youtube.com/watch?v=Xi52tx6phRU
"""
import csv
import pandas as pd
#from datetime import datetime
#print(dir(csv))

path = "C:\Python_CSV\Google_Stock.csv"


#file = open(path)

#for line in file:
#    print (line)

file = open(path, newline= '')
reader = csv.reader(file)

header = next(reader)
data = [row for row in reader]

print(header)
print(data[0])  

df = pd.read_csv(path)

print(df)

df["Swing"] = df["High"] - df["Low"]

print(df)

df = df.sort_values(by=['Swing'], ascending=False)

print(df)