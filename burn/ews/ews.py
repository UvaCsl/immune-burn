import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

import statsmodels.api as sm
import statsmodels.formula.api as smf

import pymannkendall as mk

from statsmodels.stats.diagnostic import het_white
from statsmodels.compat import lzip
from patsy import dmatrices

from scipy.stats import skew, kurtosis
from itertools import product


from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt


# used to detrend
def difference(dataset, interval = 1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return np.array(diff)


def roll_window(dataset, win_size, func):
    return dataset.rolling(int(win_size), center=True).apply(func)

def do_ews_std(dataset, time, win_size):
    return dataset.rolling(int(win_size), center=True).std()

def do_ews_skew(dataset, time, win_size):
    return dataset.rolling(int(win_size)).apply(skew)

def do_ews_kurt(dataset, time, win_size):
    return dataset.rolling(int(win_size)).apply(kurtosis)

def get_auto(dataset, lag=1):
    return sm.tsa.acf(dataset)[lag]

def do_ews_auto(dataset, time, win_size, lag=1):
    return dataset.rolling(int(win_size)).apply(get_auto)

def get_ch(dataset, time):
    df = pd.DataFrame(dataset)
    df['Time'] = time.loc[dataset.index]
    df[f'LOG_'] = np.log(dataset)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.dropna()
    if df.empty:
        return np.nan
    expr = f'LOG_ ~ Time'
    y, X = dmatrices(expr, df, return_type='dataframe')
    olsr_results = smf.ols(expr, df).fit()
    keys = ['Lagrange Multiplier statistic:', 'LM test\'s p-value:', 'F-statistic:', 'F-test\'s p-value:']
    results = het_white(olsr_results.resid, X)
#     lzip(keys, results)
    return results[1]

def do_ews_ch(dataset, time, win_size):
    return dataset.rolling(int(win_size)).apply(get_ch, args =(time,) )

def do_ar(dataset, lag=1):
    try:
        model = AutoReg(dataset, lags=lag)
        model_fit = model.fit()
        return model_fit.params[1]
    except Exception as e: 
        print(f"Warning: {e}")
        return np.nan

def do_ews_ar(dataset, time, win_size, lag=1):
    return dataset.rolling(int(win_size)).apply(do_ar)

def do_mann_kendall(noise_name, to_test, ts_name):
    ml_result = mk.original_test(to_test)
    
    print (f'{noise_name} Mann Kendall Test Results: {ts_name}')
    print ('-------------------------')
    print(f'Trend : {ml_result.trend}')
    print(f'h : {ml_result.h}')
    print(f'p : {ml_result.p}')
    print(f'Tau : {ml_result.Tau}')
    print(f'Slope : {ml_result.slope}')
    print(' ')
    print(' ')

def plot(data,
         immune,
         noise_name,
         immune_name,
         method_name,
         method,
         win_size,
         time='Time',
         nrows=2,
         log=False,
         w=6,
         supfs = 18,
         res_color= 'red'):
    
    df = data.dropna().reset_index()
    diff = pd.DataFrame(difference(data[immune]))
    
    orig = method(data[immune], data[time], win_size)
    resid = method(diff, data[time], win_size)
    
    do_mann_kendall(noise_name, orig, "Original")
    do_mann_kendall(noise_name, resid, "Residual")
    
    
    if log:
        nrows = 3
        w = 7

    fig, axes = plt.subplots(nrows=nrows, ncols=2, figsize=(w, 5))
    fig.suptitle(noise_name + ' : ' + immune_name, fontsize=supfs)
 

    axes[0, 0].plot(data[immune])
    axes[0, 0].set_title("Data")
    axes[0, 0].set_xlabel("Timestep")

    axes[0, 1].plot(diff)
    axes[0, 1].set_title("Residuals")
    axes[0, 1].set_xlabel("Timestep")

    axes[1, 0].plot(orig, color=res_color)
    axes[1, 0].set_title(method_name + " on Data")
    axes[1, 0].set_xlabel("Timestep")

    axes[1, 1].plot(resid, color=res_color)
    axes[1, 1].set_title(method_name + " on Residuals")
    axes[1, 1].set_xlabel("Timestep")

    if log:
        axes[2, 0].plot(method(np.log10(data[immune]), data[time], win_size))
        axes[2, 0].set_title("Log Data")
        axes[2, 0].set_xlabel("Timestep")

        axes[2, 1].plot(method(np.log10(diff), data[time], win_size), color=res_color)
        axes[2, 1].set_title(method_name + " on Log Residuals")
        axes[2, 1].set_xlabel("Timestep")

    fig.tight_layout()
    
    
    