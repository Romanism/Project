# 0. basic
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# 1. EDA
import seaborn as sns
sns.set()
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import *

import datetime as dt


from sklearn.preprocessing import LabelEncoder

def category_to_ohe(train_col, test_col):

    '''
    Train / Test 데이터에서 카테고리 데이터에 라벨링을 하기 위한 함수입니다.
    '''

    le = LabelEncoder()
    le.fit(train_col)

    labeled_train_col = le.transform(train_col)
    labeled_train_col = labeled_train_col.reshape(len(labeled_train_col),1)

    labeled_test_col = le.transform(test_col)
    labeled_test_col = labeled_test_col.reshape(len(labeled_test_col),1)

    return labeled_train_col, labeled_test_col
