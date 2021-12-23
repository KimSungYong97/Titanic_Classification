# 타이타닉 생존자 예측

|실험 요인|--|
|----|--|
| data 출처 | Kaggle |
| MLFramework | PyTorch |
| Model | XGBoost |
| 실험1 | 일반적인 실행 |
| 실험2 | feature 추가 (이름 속 경어 발췌 (Mr,Mrs...) |
| 실험3 | feature 추가 2 (가족 수 추가 (형제,자매,배우자 수(SibSp) + 부모,자식 수(Parch))) |
| 실험4 | RandomSearch를 통한 하이퍼 파라미터 튜닝 |

# 실험 1

### 일반적인 실행

<img src="https://user-images.githubusercontent.com/29745280/147054696-a04b09f8-5954-40f6-94a8-e1c87e3691bf.png" width="400" height="400"/>

<img src="https://user-images.githubusercontent.com/29745280/147054769-968f1c98-2e5e-43eb-a6ad-de15d7ece3ba.png" width="400" height="400"/>

오차행렬 : 

| 155 | 10 |
|---|---|
| 42 | 61 |

accuracy : 0.8060

precision : 0.8592

recall : 0.5922

AUC : 0.8171


# 실험 2

### feature 추가 (이름)

<img src="https://user-images.githubusercontent.com/29745280/147054951-72e21b41-3e7e-48b0-a27c-abfc9c32a18c.png" width="400" height="400"/>

<img src="https://user-images.githubusercontent.com/29745280/147054940-ed080675-5b44-4ca7-90a6-a1da0e4eecea.png" width="400" height="400"/>

오차행렬 : 

| 127 | 38 |
|---|---|
| 18 | 85 |

accuracy : 0.7910

precision : 0.6911

recall : 0.8252

F1 score : 0.7522

AUC : 0.8218


# 실험 3

### feature 추가 (가족 수)

<img src="https://user-images.githubusercontent.com/29745280/147054945-67ab68c5-8020-4278-bdc1-4f5e1ce86d6b.png" width="400" height="400"/>

<img src="https://user-images.githubusercontent.com/29745280/147054949-d0b55070-317b-4b2b-b621-47ab9101e68e.png" width="400" height="400"/>

오차행렬 : 

| 127 | 38 |
|---|---|
| 19 | 84 |


accuracy : 0.7873

precision : 0.6885

recall : 0.8155

F1 score : 0.7467

AUC : 0.8299


# 실험 4

### 하이퍼 파라미터 튜닝

<img src="https://user-images.githubusercontent.com/29745280/147054799-ce6ac732-6dd9-4201-a674-b09ca02ae5d0.png" width="400" height="400"/>

<img src="https://user-images.githubusercontent.com/29745280/147054842-2a0eb6f2-cd4f-49df-84b0-c81f6f22709e.png" width="400" height="400"/>

오차행렬 : 

| 133 | 32 |
|---|---|
| 27 | 76 |

accuracy : 0.7799

precision : 0.7037

recall : 0.7379

F1 score : 0.7204

AUC : 0.8348


# 실험 결과

| 실험 | 결과 |
|---|---|
| 실험 1 | 0.8171 |
| 실험 2 | 0.8218 |
| 실험 3 | 0.8299 |
| 실험 4 | 0.8348 |

# 실험 고찰

머신러닝 설계는 

데이터전처리 -> 모델 설계 -> 하이퍼파라미터 튜닝 

순으로 설계된다.

설계와 성능 향상의 중요성은 비슷한데

데이터 >>>>>>>>>>>>> 모델 >>> 하이퍼 파라미터

순으로 정확도가 달라진다.

95%의 성능을 내는 Task가 있다면 

데이터 75%, 모델 17%, 하이퍼 파리미터 3% 정도로 비중을 갖고있다고 생각한다.


본 실험에서는 데이터를 어떻게 전처리 하냐에 따른 성능 변화와 하이퍼 파라미터를 조정했을 때의 성능 변화를 측정해 보았다.

똑같은 데이터를 사용했지만 데이터의 변환 (이름, 가족, one-hot 인코딩 등) 에 따라 성능이 변할 수 있다는 것을 보여준다.

물론 다른 피처들의 변환 (ex 연속형 데이터의 범주화(나이를 연령대로 나눈다던지..), 가족이 있냐 없냐 여부(가족 수가 아닌 있는지 없는지)) 를 통해 성능을 더 높힐 수 있겠지만 본 실험에서는 배제했다.

머신러닝에서 성능을 높히기 위한 방법이 많지만 주니어 머신러닝 엔지니어로써는 모델의 동작방식, 데이터의 인풋 아웃풋을 통해 기존의 데이터에서 더 유의미한 정보를 이끌어내는 아이디어가 가장 중요하다고 생각한다.

그러기 위해서는 해당 Task에 대한 도메인 지식, 모델에 대한 높은 이해도, 그리고 최근 연구 트렌드를 따라가는 노력이 매우매우매우 필요하다고 생각한다.

더 발전하면 모델 설계도 도전해보는걸로...
