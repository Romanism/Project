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
import scipy as sp
