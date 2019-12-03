# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:25:26 2019

@author: Satish
https://www.youtube.com/watch?v=Xi52tx6phRU
"""
import csv
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

'''
data = []

for row in reader:
    # row = [Date, Open, High, low, Close, Volume, Adj. Close]
    date= datetime.strpttime(row[0], '%m%d%Y')

open_price = float(row[1])
high = float(row[2])
low = float(row[3])
close = float(row[4])
volume = float(row[5])
adj_close = float(row[6])

data1.append([date, open_price, high, low, close, volume, adj_close])

'''   