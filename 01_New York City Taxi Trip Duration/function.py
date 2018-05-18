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
