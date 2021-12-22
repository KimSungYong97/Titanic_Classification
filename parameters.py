
param_init = {'n_estimators': 100,
              'max_depth': 3,
              'learning_rate': 0.003,

              'subsample': 1,
              'scale_pos_weight': 1,
              'reg_lambda': 1,
              'reg_alpha': 0,
              'objective': 'binary:logistic',
              'min_split_loss': 0,
              'min_child_weight': 1,
              'eval_metric': 'error',
              'colsample_bytree': 1
              }


param_grid = {

    'n_estimators': range(50, 1050, 50),
    'max_depth': range(3, 12, 1),
    'learning_rate': [i/100 for i in range(1,51)],
    'min_child_weight': [1],
    'min_split_loss': [0],
    'subsample': [1],
    'reg_lambda': [1],
    'reg_alpha': [0],
    'scale_pos_weight': [1],
    'colsample_bytree': [1],
    'objective': ['binary:logistic'],
    'eval_metric': ['error']
}
'''
    {'learning_rate': leaning_rate,
          # 학습률 0.3
          'n_estimators': n_estimators,
          # 생성할 weak learner 수 100
          'min_child_weight': 1,
          # - GBM의 min_samples_leaf와 유사
          # - 관측치에 대한 가중치 합의 최소를 말하지만GBM에서는 관측치 수에 대한 최소를 의미
          # - 과적합 조절 용도
          # - 범위: 0 ~ ∞
          'min_split_loss': 0,
          # - 리프노드의 추가분할을 결정할 최소손실 감소값
          # - 해당값보다 손실이 크게 감소할 때 분리
          # - 값이 클수록 과적합 감소효과
          # - 범위: 0 ~ ∞
          'max_depth': max_depth,
          # - 트리 기반 알고리즘의 max_depth와 동일
          # - 0을 지정하면 깊이의 제한이 없음
          # - 너무 크면 과적합(통상 3~10정도 적용)
          # - 범위: 0 ~ ∞
          # 6
          'subsample': 1,
          # - GBM의 subsample과 동일
          # - 데이터 샘플링 비율 지정(과적합 제어)
          # - 일반적으로 0.5~1 사이의 값을 사용
          # - 범위: 0 ~ 1
          'reg_lambda': 1,
          # - L2 Regularization 적용 값
          # - 피처 개수가 많을 때 적용을 검토
          # - 클수록 과적합 감소 효과
          'reg_alpha': 0,
          # L1 Regularization 적용 값
          # - 피처 개수가 많을 때 적용을 검토
          # - 클수록 과적합 감소 효과
          'scale_pos_weight': 1,
          # 불균형 데이터셋의 균형을 유지
          'colsample_bytree': 1,
          # - GBM의 max_features와 유사
          # - 트리 생성에 필요한 피처의 샘플링에 사용
          # - 피처가 많을 때 과적합 조절에 사용
          # - 범위: 0 ~ 1
          'objective': 'binary:logistic',
          # - ‘reg:linear’ : 회귀
          # - binary:logistic : 이진분류
          # - multi:softmax : 다중분류, 클래스 반환
          # - multi:softprob : 다중분류, 확륣반환
          'eval_metric': 'error',
          # - 검증에 사용되는 함수정의
          # - 회귀 분석인 경우 'rmse'를, 클래스 분류 문제인 경우 'error'
          # ----------------------------------------------------
          # - rmse : Root Mean Squared Error
          # - mae : mean absolute error
          # - logloss : Negative log-likelihood
          # - error : binary classification error rate
          # - merror : multiclass classification error rate
          # - mlogloss: Multiclass logloss
          # - auc: Area Under Curve
          'early_stoppings' : 100
          # 조기중단을 위한 최소 반복횟수
          }'''

'''
    과적합 제어
    eta 값을 낮춥니다.(0.01 ~ 0.1) → eta 값을 낮추면 num_boost_round(n_estimator)를 반대로 높여주어야 합니다.
    max_depth 값을 낮춥니다.
    min_child_weight 값을 높입니다.
    gamma 값을 높입니다.
    subsample과 colsample_bytree를 낮춥니다.
    '''
