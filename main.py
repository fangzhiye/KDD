# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
import xgboost as xgb

# Read in our input data
df_train = pd.read_csv('./input/TrainData.csv')
df_test = pd.read_csv('./input/TestData.csv')

# This prints out (rows, columns) in each dataframe
print('Train shape:', df_train.shape)
print('Test shape:', df_test.shape)

print('Columns:', df_train.columns)

y_train = df_train['is_risk'].values
id_train = df_train['rowkey'].values
id_test = df_test['rowkey'].values
'''
for i in range(m_trade):
    df_train.loc[i,'time'] = ISOString2Time(df_train.loc[i,'time'][0:19])
print('43line')    
for i in range(m_login):
    train_login.loc[i,'time'] = ISOString2Time(train_login.loc[i,'time'][0:19])
 '''   
df_train = df_train.rename(columns={'tradeTime':'tradetime'})
df_train['logis_scan'] = df_train['logis_scan'].astype('bool')
df_train['logis_sec'] = df_train['logis_sec'].astype('bool')
df_test['logis_scan'] = df_test['logis_scan'].astype('bool')
df_test['logis_sec'] = df_test['logis_sec'].astype('bool')
# We drop these variables as we don't want to train on them
# The other 57 columns are all numerical and can be trained on without preprocessing
x_train = df_train.drop(['is_risk', 'id','tradetime','logtime'], axis=1)#remove target id columns
x_test = df_test.drop(['id','tradetime','logtime'], axis=1)
# Take a random 20% of the dataset as validation data
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.2, random_state=4242)
print('Train samples: {} Validation samples: {}'.format(len(x_train), len(x_valid)))

# Convert our data into XGBoost format
d_train = xgb.DMatrix(x_train, y_train)
d_valid = xgb.DMatrix(x_valid, y_valid)
d_test = xgb.DMatrix(x_test)

# Set xgboost parameters
params = {}
params['objective'] = 'binary:logistic'
params['eta'] = 0.02
params['silent'] = True
params['max_depth'] = 6
params['subsample'] = 0.9
params['colsample_bytree'] = 0.9

# Define the gini metric - from https://www.kaggle.com/c/ClaimPredictionChallenge/discussion/703#5897

def gini(actual, pred, cmpcol = 0, sortcol = 1):
    
    assert( len(actual) == len(pred) )
    all = np.asarray(np.c_[ actual, pred, np.arange(len(actual)) ], dtype=np.float)
    all = all[ np.lexsort((all[:,2], -1*all[:,1])) ]
    totalLosses = all[:,0].sum()
    giniSum = all[:,0].cumsum().sum() / totalLosses
    
    giniSum -= (len(actual) + 1) / 2.
    return giniSum / len(actual)
 
def gini_normalized(a, p):
    return gini(a, p) / gini(a, a)

# Create an XGBoost-compatible metric from Gini

def gini_xgb(preds, dtrain):
    labels = dtrain.get_label()
    gini_score = gini_normalized(labels, preds)
    return [('gini', gini_score)]
# This is the data xgboost will test on after eachboosting round
watchlist = [(d_train, 'train'), (d_valid, 'valid')]

# Train the model! We pass in a max of 10,000 rounds (with early stopping after 100)
# and the custom metric (maximize=True tells xgb that higher metric is better)
mdl = xgb.train(params, d_train, 10000, watchlist, early_stopping_rounds=100, feval=gini_xgb, maximize=True, verbose_eval=10)

# Predict on our test data
p_test = mdl.predict(d_test)

# Create a submission file
sub = pd.DataFrame()
sub['rowkey'] = id_test
sub['is_risk'] = p_test
sub.to_csv('PredictTrade.csv', index=False)

print(sub.head())
