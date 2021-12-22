from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBClassifier
import pandas as pd

import parameters

def param(x_train, y_train,mode):
    if(mode == 'init'):
        return parameters.param_init
    elif(mode =='random_search'):
        # XGBoost 분류기 생성
        xgb_clf = XGBClassifier()

        # 초모수 격자생성
        xgb_param_grid = parameters.param_grid

        # Create a random search object
        xgb_random = RandomizedSearchCV(estimator=xgb_clf,
                                        param_distributions=xgb_param_grid,
                                        n_iter=50,
                                        scoring='roc_auc',
                                        cv=10,
                                        refit=True,
                                        return_train_score=True)

        # Fit to the training data
        pd.set_option('display.max_columns', None)
        xgb_random.fit(x_train, y_train)
        hr_random_df = pd.DataFrame(xgb_random.cv_results_)
        hr_random_df.to_csv('params.csv')
        params=hr_random_df.loc[hr_random_df['mean_test_score'].idxmax(), ["params"]]
        print(params)
        return params["params"]