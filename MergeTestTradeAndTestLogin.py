#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:16:40 2017

@author: zhenfang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:17:49 2017

@author: zhenfang
"""

import pandas as pd
import numpy as np
#import time
#import datetime

stdtime = '2017-11-01 12:00:00'
lStdTime = len(stdtime)
dayseconds = 24*3600*30*6

test_login = pd.read_csv('./input/t_login_test.csv')
test_trade = pd.read_csv('./input/preTestTrade.csv')
#train_trade = pd.read_csv('./input/newPreTrade.csv')
#originTrade = pd.read_csv('./input/t_trade.csv')
#originTrade = originTrade.sort_values(by = ['id','time'],ascending = False)
#originTrade.rename(columns={'time':'tradeTime'})
#train_trade = pd.concat([train_trade,originTrade['tradeTime']],axis = 1)
test_login = test_login.sort_values(by = ['id','timestamp'],ascending = True)
test_trade = test_trade.sort_values(by = ['id', 'time'],ascending = True)
[m_login,n_login] = test_login.shape
[m_trade,n_trade] = test_trade.shape

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
test_trade['logtimelong'] = np.nan
test_trade['logdevice'] = np.nan
test_trade['log_from'] = np.nan
test_trade['logip'] = np.nan
test_trade['logcity'] = np.nan
test_trade['logresult'] = np.nan
test_trade['logtimestamp'] = np.nan
test_trade['logtype'] = np.nan
test_trade['logis_scan'] = np.nan
test_trade['logis_sec'] = np.nan
test_trade['logtime'] = ''

preTrades = 0
preLogId = 0
isCount = False
idSum = 0   
#m_login = 500
#m_trade = 300
for i in range(m_login):
    
    logId = test_login.iloc[i,9]
    logTime = test_login.iloc[i,7]
    if not logId == preLogId: isCount = True
    else: isCount = False
    if not logId == preLogId: preTrades = idSum
   # print('logId',logId)
    if i%1000 == 0: print('logId:',logId)
    #if logId == 330: print('330')
   # print('idSum',idSum)
    for j in range (preTrades,m_trade):
        
      #  idSum = idSum + 1
       # print('j',j)
        #print('isCount',isCount)
        tradeId = test_trade.iloc[j,2]
       # print('tradeId:',tradeId)
       # nextTradeTime = 0
        if logId == tradeId:
                preLogId = logId
                if isCount: 
                    idSum = idSum + 1
                '''
                if  not train_trade.iloc[j,15] is None:
                    continue
                '''
               # print('tradeId',tradeId)
                curTradeTime = test_trade.iloc[j,3]
               #print('curLogTime:'+curLogTime)
               # nextTradeTime = 0
               # if  tradeId == train_trade.iloc[j+1]['id'] : 
                   # nextTradeTime = train_trade.iloc[j+1]['time']
                   # print('nextLogTime:'+nextLogTime)
                if  logTime < curTradeTime :
                #    print('logiId:isrisk_:')
                 #   print(train_trade.iloc[i]['is_risk'])
                    test_trade.iloc[j,4] = test_login.iloc[i,1]
                    test_trade.iloc[j,5] = test_login.iloc[i,2]
                    test_trade.iloc[j,6] = test_login.iloc[i,3]
                    test_trade.iloc[j,7] = test_login.iloc[i,4]
                    test_trade.iloc[j,8] = test_login.iloc[i,5]
                    test_trade.iloc[j,9] = test_login.iloc[i,6]
                    test_trade.iloc[j,10] = test_login.iloc[i,7]
                    test_trade.iloc[j,11] = test_login.iloc[i,8]
                    test_trade.iloc[j,12] = test_login.iloc[i,10]
                    test_trade.iloc[j,13] = test_login.iloc[i,11]
                    test_trade.iloc[j,14] = test_login.iloc[i,12]
                    
                    #train_trade.iat[j,15] = train_login.iloc[i,0]
                else: continue
        elif logId > tradeId : 
            preLogId = logId
            continue 
        else :
            preLogId = logId
            break
test_login.to_csv('newTestlogin.csv',index=False)
test_trade.to_csv('newTesttrade.csv',index=False)
   
    



