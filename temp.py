#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:17:49 2017

@author: zhenfang
"""

import pandas as pd
import numpy as np
import time
import datetime

stdtime = '2017-11-01 12:00:00'
lStdTime = len(stdtime)

train_login = pd.read_csv('./input/preTrainLogin.csv')
train_trade = pd.read_csv('./input/preTrainTrade.csv')

[m_login,n_login] = train_login.shape
[m_trade,n_trade] = train_trade.shape

#train_login = login.sort_values(by = ['id','time'],ascending = True)
#train_trade = trade.sort_values(by = ['id','time'],ascending = True)


'''
def ISOString2Time(s):
    d = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
    return time.mktime(d.timetuple())
'''
'''
for i in range(m_trade):
    if  train_trade.loc[i,'is_risk'] is None :
        train_trade.drop(i)
'''
'''
for i in range(m_trade):
        temp = train_trade.loc[i,'time'].strip('.0')
        lTime = len(temp)
        if lTime == lStdTime :
             train_trade.loc[i,'time'] = ISOString2Time()
        else :
            for i in [lTime,lStdTime]:
                temp=temp + '0'
        train_trade.loc[i,'time'] = ISOString2Time(temp)
 '''  
'''   
print('40line')  
for i in range(m_trade):
    train_trade.loc[i,'time'] = ISOString2Time(train_trade.loc[i,'time'][0:19])
print('43line')    
for i in range(m_login):
    train_login.loc[i,'time'] = ISOString2Time(train_login.loc[i,'time'][0:19])
    
print('47line') 
'''
#train_trade.iat[0,3]=1
m_trade = 5
m_login = 10
train_login['is_risk'] = 0
train_login['rowkey'] = 0
train_login['tradetime'] = ''
preTrades = 0
idSum = 0   
for i in range(m_login):
    tradeId = train_trade.iloc[i]['id']
    tradeTime = train_trade.iloc[i]['time']
   # print('tradeTime:'+tradeTime)
   # is_risk = train_trade.iloc[i]['is_risk']
    preTrades = idSum
    print('tradeId:',tradeId)
    for j in range (preTrades,m_trade):
        idSum = idSum + 1
        logId = train_login.iloc[j]['id']
        #print('logId:',logId)
        if logId == tradeId:
                curLogTime = train_login.iloc[j]['time']
               # print('curLogTime:'+curLogTime)
                nextLogTime = '9090-11-11 24:00:00'
                if logId == train_login.iloc[j+1]['id'] : 
                    nextLogTime = train_login.iloc[j+1]['time']
                   # print('nextLogTime:'+nextLogTime)
                if  not nextLogTime is None and tradeTime > curLogTime and tradeTime < nextLogTime:
                #    print('logiId:isrisk_:')
                 #   print(train_trade.iloc[i]['is_risk'])
                    train_login.iat[j,13] = train_trade.iloc[i]['is_risk']
                    train_login.iat[j,14] = train_trade.iloc[i]['rowkey']
                    train_login.iat[j,15] = train_trade.iloc[i]['time']
                    break
                else: continue
        elif tradeId > logId : continue 
        elif tradeId < logId  : break
train_login.to_csv('newlogin.csv',index=False)
train_trade.to_csv('newtrade.csv',index=False)
        
    



