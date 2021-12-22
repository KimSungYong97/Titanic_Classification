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

