# 0. basic
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# 1. EDA
import seaborn as sns
sns.set()
sns.set_style("whitegrid")
sns.set_color_codes(palette="muted")
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import *

# 2. preprocessing
import datetime as dt
import holidays

def holiday(x):

    '''
    휴일이면 1, 휴일이 아니면 0으로 표시해주는 함수입니다.
    '''
    us_holidays = holidays.US(state='NY', years=2016)
    if x in us_holidays:
        return 1
    else:
        x = x.weekday()
    if x > 4:
        return 0
    else:
        return 0

def haversine_np(lon1, lat1, lon2, lat2):

    '''
    위도 경도 좌표를 이용해 두 지점간의 거리를 표시해주는 함수입니다. 단위는 km입니다.
    '''

    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c

    return km

# 3. Modeling
import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
import scipy as sp
from patsy import dmatrix


# outlier
def cooks_distace(result, data, category=False, dropped=False):

    '''
    Cook's distance를 활용한 아웃라이어 제거 함수입니다.
    Cook's distance를 통해 제거된 데이터들은 dropped_data로 따로 저장했습니다.
    '''

    influence = result.get_influence()

    if category:
        fox_cr = 4 / (len(data) - result.df_model + 1)
    else:
        fox_cr = 4 / (len(data) - result.df_model)

    cooks_d2, pvals = influence.cooks_distance
    idx = np.where(cooks_d2 > fox_cr)[0]

    dropped_data = data.iloc[idx]
    data = data.drop(data.index[idx])
    data.reset_index(drop=True, inplace=True)

    if dropped:

        return data, dropped_data

    return data


# storage
def storage(result, result_sets, remark) :
    """
    test storage
    """
    result.summary()
    put = {
        "R-square" :round(result.rsquared, 3),
        "AIC" : round(result.aic, 3),
        "BIC" : round(result.bic, 3),
        "Pb(Fstatics)" : round(result.f_pvalue, 3),
        "Pb(omnibus)" : round(result.diagn['omnipv'], 3),
        "Pb(jb)" : round(result.diagn['jbpv'], 3),
        "Cond.No." : round(result.diagn['condno'], 3),
        "Dub-Wat": round(durbin_watson(result.wresid), 3),
        "Remarks" : remark,
    }
    result_sets.loc[len(result_sets)] = put
