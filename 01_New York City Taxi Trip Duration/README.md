# Regression Project : New York City Taxi Trip Duration
[New York City Taxi Trip Duration Link](https://www.kaggle.com/c/nyc-taxi-trip-duration)


### 1. Team : Adaptor
- 강동수 [팀장]
- 김문수 [팀원]
- 지성인 [팀원]



### 2. Project Period
- 시작일 : 2018/02/03
- 종료일 : 2018/03/14
- 발표일 : 2018/03/15



### 3. Overview

#### 3.1 Description

Kaggle is challenging you to build a model that predicts the total ride duration of taxi trips in New York City.


: 뉴욕시에서 택시 주행시간을 예측하는 것이 목적


#### 3.2 Evaluation (RMSLE)
<img src="img/RMSLE.png" width="500">

- ϵ - RMSLE value (score)
- n - total number of observations in the (public/private) data set
- pi - prediction of trip duration
- ai - actual trip duration
- log(x) - natural logarithm


: 예측값과 실제값의 차이를 통한 점수 부여 (값이 낮을 수록 예측값이 실제값에 가까워 좋은 예측임을 의미)



### 4. Data

#### 4.1 Data set
- train.csv - the training set (contains 1,458,644 trip records)
- test.csv - the testing set (contains 625,134 trip records)
- sample_submission.csv - a sample submission file in the correct format


#### 4.2 Data fields
- id - 운행 고유 id
- vendor_id - 택시 회사 id (0/1)
- pickup_datetime - 승차 시간
- dropoff_datetime - 하차 시간
- passenger_count - 승객 수
- pickup_longitude - 승차 위도
- pickup_latitude - 승차 경도
- dropoff_longitude - 하차 위도
- dropoff_latitude - 하차 경도
- store_and_fwd_flag - 주행 기록시 차량 메모리 저장 여부 (Y: 저장/전송, N: 미저장/전송)
- trip_duration - 주행시간 (초)



### 5. Modeling


#### 5.1 EDA
- 독립변수 ($X$)
  - 개별 EDA 실시
  - EDA를 통한 이상치 제거
  - 좌표 데이터를 통한 거리 생성
  - 시간 데이터를 월/일/시간/분 단위로 쪼갬
  - 변수간 상관관계 파악 (Heatmap)
  - 다중공선성 파악 (VIF)

- 종속변수 ($y$)
  - Normal 분포를 통한 정규성 확인
  - Boxplot을 통한 이상치 제거


#### 5.2 데이터 검정
- 잔차정규성 검정
- Residual-Feature 관계 검정
- 이분산 검정
- 자기상관 검정


#### 5.3 최적 정규화
- OLS를 통한 모델링 생성
- Feature 선정


#### 5.4 Modeling
- 1차 모델링
  - origin modeling
- 2차 모델링
  - 아웃라이어 1회 제거 (cook's distance)
- 3차 모델링
  - 아웃라이어 2회 제거 (cook's distance)



### 6 submission
- Paticipate teams : 1,076
- Final Score : 0.50829
- Leaderboard : 808 / 1257 (64%)

<img src="img/submission.png" width="700">
