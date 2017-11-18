#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:50:19 2017

@author: zhenfang
"""
import pandas as pd
import numpy as np
import time
import datetime
stdtime = '2017-11-01 12:00:00'
lStdTime = len(stdtime)

train_login = pd.read_csv('./input/t_login.csv')
train_trade = pd.read_csv('./input/t_trade.csv')

[m_login,n_login] = train_login.shape
[m_trade,n_trade] = train_trade.shape

def ISOString2Time(s):
    d = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
    return time.mktime(d.timetuple())
 
#for i in range(m_trade):
temp = '2017-01-01 01:'
lTime = len(temp)
for i in [lTime,lStdTime]:
    temp=temp + '0'
        #train_trade.loc[i,'time'] = ISOString2Time(temp)
#train_login.
#train_trade.sort_values(by = ['id','time'],ascending = True)

#def ISOString2Time(s):
  #  d = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
 #   return time.mktime(d.timetuple())

#S=ISOString2Time(train_trade.loc[1,'time'])
#for i in range(m_trade):
#    train_trade.loc[i,'time'] = ISOString2Time(train_trade.loc[i,'time'])