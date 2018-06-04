# 출처 : https://github.com/aparna-k/DataScienceExperiments/blob/master/avito-prediction-challenge/translate_avito_title_descriptions.py

import pandas as pd
import sys
import textblob
from tqdm import tqdm,tqdm_pandas


def desc_missing(x):
    '''
    Takes data frame as input, then searches and fills missing description with недостающий
    '''
    if x['description'].isnull().sum()>0:
        print("Description column has missing values, filling up with недостающий")
        x['description'].fillna("недостающий",inplace=True)
        return x
    else:
        return x

def translate(x):
    try:
        return textblob.TextBlob(x).translate(to="en")
    except:
        return x

def map_translate(x):
    print("Begining to translate")
    tqdm.pandas(tqdm())
    x['region']=x['region'].progress_map(translate)
    x['city']=x['city'].progress_map(translate)
    x['parent_category_name']=x['parent_category_name'].progress_map(translate)
    x['param_1']=x['param_1'].progress_map(translate)
    x['param_2']=x['param_2'].progress_map(translate)
    x['param_3']=x['param_3'].progress_map(translate)
    x['title']=x['title'].progress_map(translate)
    x['description']=x['description'].progress_map(translate)
    return x

def exporter(x,dest_path):
    print("Writting to {}".format(dest_path))
    x.to_csv(dest_path,index=False)
    print("Done")

def main():
    file=sys.argv[1]
    dest=sys.argv[2]
    data=read(file)
    data=desc_missing(data)
    data=map_translate(data)
    exporter(data,dest)
