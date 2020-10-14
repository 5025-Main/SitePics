# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:42:40 2020

@author: alex.messina
"""
import os

datadir = 'C:/Users/alex.messina/Documents/GitHub/SitePics/'

for f in os.listdir(datadir):
    if f.endswith('.jpg') == False:
        if f.startswith('.git')==False:
            print f
            print f.split('.')[0]
            os.rename(datadir+f, datadir + f.split('.')[0] + '.jpg')
            