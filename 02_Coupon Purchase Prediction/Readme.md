# Classification Project : Coupon Purchase Prediction
[Project Link](https://github.com/Anylee2142/dss7-coupon/blob/master/Presentation/presentation_datanism.ipynb)


## Team : Datanism
- 지성인 [팀장]
- 이재웅 [팀원]
- 이준성 [팀원]


## Project Period
- 시작일 : 2018/03/23
- 종료일 : 2018/04/10
- 발표일 : 2018/04/11


## Overview

#### Description

Using past purchase and browsing behavior, this competition asks you to predict which coupons a customer will buy in a given period of time.


:  주어진 기간동안 고객들이 어떤 쿠폰을 구입할 지 예측하는 문제


#### Evaluation (RMSLE)
<img src="img/MAP.png" width="500">

- |U| - number of users
- P(k) - precision at cutoff k
- n - number of predicted coupons
- m - number of purchased coupons for the given user. If m = 0, the precision is defined to be 0


## Data

#### Data set
- user_list.csv - the master list of users in the dataset
- coupon_list_train.csv - the master list of coupons which are considered part of the training set
- coupon_list_test.csv - the master list of coupons which are considered part of the test set. Your competition predictions should be sourced only from these 310 coupons. You will not receive credit for predicting training set coupons that were purchased during the test set period.
- coupon_visit_train.csv - the viewing log of users browsing coupons during the training set time period. You are not provided this table for the test set period.
- coupon_detail_train.csv - the purchase log of users buying coupons during the training set time period. You are not provided this table for the test set period.
- coupon_area_train.csv - the coupon listing area for the training set coupons
- coupon_area_test.csv - the coupon listing area for the test set coupons
- sample_submission.csv - a sample file showing the correct format for predictions
- documentation.zip - an archive of Excel files containing an entity relationship diagram and English translations


#### Data fields
- [Jupeter Notebook](https://github.com/Anylee2142/dss7-coupon/blob/master/Presentation/presentation_datanism.ipynb) 참고


## Modeling


#### 1. Data set
- 각 테이블 변수 파악
- 테이블간 구조 파악


#### 2. EDA
- 지역과 관련된 Data EDA
- 가격과 관련된 Data EDA
- 쿠폰종류와 관련된 Data EDA


#### 3. Modeling

- Feature select
  - CAPSULE_TEXT
  - DISCOUNT_PRICE
  - large_area_name
  - ken_name
  - small_area_name

- Model select
  - Cosine similarity


#### 4. Submission
- Paticipate teams : 1,076
- Final Score : 0.0063885
- Leaderboard : 69 / 1076 (6.4%)

<img src="img/submission.png" width="700">
