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
dayseconds = 24*3600

train_login = pd.read_csv('./input/preTrainLogin.csv')
train_trade = pd.read_csv('./input/newPreTrade.csv')
#originTrade = pd.read_csv('./input/t_trade.csv')
#originTrade = originTrade.sort_values(by = ['id','time'],ascending = False)
#originTrade.rename(columns={'time':'tradeTime'})
#train_trade = pd.concat([train_trade,originTrade['tradeTime']],axis = 1)

[m_login,n_login] = train_login.shape
[m_trade,n_trade] = train_trade.shape

#train_login = login.sort_values(by = ['id','time'],ascending = False)
#train_trade = trade.sort_values(by = ['id','time'],ascending = False)
'''
def ISOString2Time(s):
    d = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
    return time.mktime(d.timetuple())

for i in range(m_trade):
    print(i)
    train_trade.loc[i,'time'] = ISOString2Time(train_trade.loc[i,'time'][0:19])

train_login.to_csv('preTrainLogin.csv',index=False)
train_trade.to_csv('preTrainTrade.csv',index=False)
'''
''''

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
train_trade['logtimelong'] = np.nan
train_trade['logdevice'] = np.nan
train_trade['log_from'] = np.nan
train_trade['logip'] = np.nan
train_trade['logcity'] = np.nan
train_trade['logresult'] = np.nan
train_trade['logtimestamp'] = np.nan
train_trade['logtype'] = np.nan
train_trade['logis_scan'] = np.nan
train_trade['logis_sec'] = np.nan
train_trade['logtime'] = ''

preTrades = 0
idSum = 0   
#m_login = 1000
#m_trade = 300
for i in range(m_login):
    logId = train_login.iloc[i]['id']
    logTime = train_login.iloc[i]['timestamp']
    preTrades = idSum
    print('logId:',logId)
    for j in range (m_trade):
        idSum = idSum + 1
        tradeId = train_trade.iloc[j]['id']
        #print('logId:',logId)
       # nextTradeTime = 0
        if logId == tradeId:
                curTradeTime = train_trade.iloc[j]['time']
               # print('curLogTime:'+curLogTime)
               # nextTradeTime = 0
               # if  tradeId == train_trade.iloc[j+1]['id'] : 
                   # nextTradeTime = train_trade.iloc[j+1]['time']
                   # print('nextLogTime:'+nextLogTime)
                if  logTime < curTradeTime  and curTradeTime - logTime <= dayseconds*7 :
                #    print('logiId:isrisk_:')
                 #   print(train_trade.iloc[i]['is_risk'])
                    train_trade.iat[j,5] = train_login.iloc[i]['timelong']
                    train_trade.iat[j,6] = train_login.iloc[i]['device']
                    train_trade.iat[j,7] = train_login.iloc[i]['log_from']
                    train_trade.iat[j,8] = train_login.iloc[i]['ip']
                    train_trade.iat[j,9] = train_login.iloc[i]['city']
                    train_trade.iat[j,10] = train_login.iloc[i]['result']
                    train_trade.iat[j,11] = train_login.iloc[i]['timestamp']
                    train_trade.iat[j,12] = train_login.iloc[i]['type']
                    train_trade.iat[j,13] = train_login.iloc[i]['is_scan']
                    train_trade.iat[j,14] = train_login.iloc[i]['is_sec']
                    train_trade.iat[j,15] = train_login.iloc[i]['time']
                else: continue
        elif logId < tradeId : continue 
        elif logId > tradeId  : break
train_login.to_csv('newlogin.csv',index=False)
train_trade.to_csv('newtrade.csv',index=False)
   
    



