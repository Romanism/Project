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


# 2. Feature Select
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


# 3. Modeling

from statsmodels.stats.outliers_influence import variance_inflation_factor

# 3.1 조건부 확률기반 생성모형
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis # LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis # QDA
from sklearn.naive_bayes import * # Naive basesian

# 3.2 조건부 확률기반 판별모형
from sklearn.tree import DecisionTreeClassifier

# 3.3 모형결합 (Ensenble)
from sklearn.ensemble import VotingClassifier # voting
from sklearn.ensemble import BaggingClassifier # bagging
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier # random Forest

from sklearn.ensemble import AdaBoostClassifier # AdaBoost
from sklearn.ensemble import GradientBoostingClassifier # GradientBoost
import xgboost # xgboost

# 3.4 판별함수 모형
from sklearn.linear_model import Perceptron # perceptron
from sklearn.linear_model import SGDClassifier # SGD
from sklearn.svm import SVC # support vector machine


# 4. Optimizer
from sklearn.model_selection import validation_curve # validation curve
from sklearn.model_selection import GridSearchCV # gridseach
from sklearn.model_selection import ParameterGrid # ParameterGrid


# 5. Evaluation
from sklearn.metrics import * # make confusion matrix
from sklearn.preprocessing import label_binarize # ROC curve
from sklearn.metrics import auc # AUC
from sklearn.metrics import roc_curve
