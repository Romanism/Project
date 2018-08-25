<h1><center>The prediction models for the premierleague</center></h1>

<center><img src="img/premierleague.jpeg" width = 800></center>

[Project Link](https://github.com/Romanism/Project/blob/master/03_Premierleague/PROJECT.pdf)
<br><br/>
### 1. Introduction

#### 1.1 period
- 시작일 : 2018/04/27
- 종료일 : 2018/05/10

#### 1.2 Description

저는 축구를 좋아하는 대한민국 평범한 남자입니다. 제가 좋아하는 팀은 프리미어리그의 아스널이란 팀인데요, 아스널의 팬인 저는 항상 사스널이라는 얘기를 들어야했습니다..후.. 아스널의 1위를 소망하는 저는 도대체 우리팀이 부족한부분이 뭔지 알고싶어졌습니다! 과연 프리미어리그에서 승리를 하기 위해선 팀이 어느 정도의 Performance를 보여줘야 할까?
그리고 아스널은 1위를 하기 위해 어떤 점을 좀 더 보완해야 할까? 라는 주제로 진행해봤습니다. 이를 위해 경기당 팀이 보여줬던 Performance를 분석해 앞으로 벌어지는 경기에 대해 예측하는 모델을 생성해보고 이를 토대로 아스널이 보완해야할 부분에 대해서도 알아봤습니다.


#### 1.3 Data set
출처 : [프리미어리그 공식 홈페이지](https://www.premierleague.com)

- Team : 팀 이름, 프리미어리그는 강등 제도가 있어 매년마다 3개의 팀이 바뀜
- Possession : 점유율 (%)
- SOT(Shots of Target) : 유효슈팅 (골문안으로 들어간 슛팅) (개)
- Shots : 슈팅 (전체 슛팅) (개)
- Touches : 공을 터치한 개수 (개)
- Passes : 패스 (개)
- Tackles : 태클 (개)
- Clearances : 골문앞에서 공을 걷어낸 개수 (개) Corners : 코너킥 (개)
- Offsides : 오프사이드 (개)
- Goal : 골 (개)
- Year : 년도 (2012, 2013, 2014, 2015, 2016, 2017)
- Home :홈 / 어웨이 여부 (어웨이:0,홈:1)
- Result :결과 (패:0,승:1,무:2)


#### 1.4 Evaluation
- Confusion Matrix
- ROC Curve
<br><br/>


## 2. PROJECT

#### 2.1 Crawling data

- Selenium활용
- 6년치 데이터, 13개의 변수 등 총 4,560개 데이터 Crawling


#### 2.2 EDA
- Overall information
- Y data
- Y data & X data
- Correlation
- F-test
- Arsenal vs Rest

#### 2.3 Modeling
- RandomForest
- GridSearch
- Cross Validation


#### 2.4 Evaluation
- Confusion Matrix
- ROC Curve
<br><br/>


## 3. Key Points
- Selenium을 활용한 데이터 Crawling
- RandomForest을 통한 Modeling
- GridSearch, Cross Validation을 통한 모델 최적화
- Confusion Matrix, ROC Curve등 분류 평가 방법을 활용


## 4. 느낀점
- 평소에 궁금하던 주제를 통해 프로젝트를 진행하다보니 재밌었다.
- 혼자서 하는 첫번째 프로젝트라는 점에서 의미가 깊었다.
- 승부에 직접적인 영향을 줄 수 있는 부상선수가 몇명 있는지, 해당 경기 전 휴식일이 얼마나 됐는지 등에 대한 데이터가 있었으면 성능이 더 잘나왔을것이라 생각한다.


## 5. 한계점
- 스포츠는 기록이 전부라고 볼 수 없다. 예를 들어 그날 선수들의 컨디션, 상대성, 감독 전술 여부 등 여러요소가 복합적으로 이뤄지는데 이를 반영하지 못한 점이 아쉬웠다.
