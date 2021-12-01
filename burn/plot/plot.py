import pandas as pd
import burn
import numpy as np

from burn.utils import *

def loop_fig(fignum):
    return fignum + 1


def get_header():
    header = ['N_R', 'AP_Eblood', 'AP_Etissue', 'AP_Eliver', 'AP_Sblood', 'AP_Stissue', 'ITMblood', 'ITMtissue',
              'M_R', 'M_A', 'CH', 'N_A', 'ND_A', 'ACH', 'ND_N', 'C_blood', 'C', 'C_A', 'C_B', 'TGF_beta']
    return header

def prep_plot(wsol, t_interval, timein, timeout, time_format=1):
    t = set_time(t_interval, timein, timeout)
    df_model = pd.DataFrame(wsol)
    keys = df_model.columns.values
    dictionary = dict(zip(keys, get_header()))
    df_model = df_model.rename(columns=dictionary)
    df_model['Time'] = np.array(t) * time_format
    
    return df_model, t
