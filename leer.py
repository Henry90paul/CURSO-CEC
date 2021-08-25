# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:35:47 2021

@author: CONTROL_1
"""
lista=[]
file=open("devices.txt")
for i in file:
    i=i.strip()
    lista.append(i)
    print(i)
file.close()
print(lista)