import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import seaborn as sns


# 3. Modeling

from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier # random Forest
from sklearn.ensemble import GradientBoostingClassifier # GradientBoost
import xgboost # xgboost


# 4. Optimizer
from sklearn.model_selection import validation_curve # validation curve
from sklearn.model_selection import GridSearchCV # gridseach
from sklearn.model_selection import ParameterGrid # ParameterGrid


# 5. Evaluation
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.metrics import * # make confusion matrix
