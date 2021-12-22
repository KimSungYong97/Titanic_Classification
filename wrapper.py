import parameters
from score import clf_eval
from score import feature_importance_plot
from score import roc_curve_plot
from score import cross_val

import hyper_tunning

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

import warnings

warnings.filterwarnings('ignore')

def Classifier(x_train, y_train, x_test, y_test):
    param = hyper_tunning.param(x_train, y_train,'init')
    #디폴트 = 'init'
    #랜덤서치 = 'random_search
    xgb_wrapper = XGBClassifier(**param)
    val_xgb_wrapper = XGBClassifier(**param)

    val_x_train, val_x_test, val_y_train, val_y_test = train_test_split(x_train, y_train,
                                                                        test_size=0.3,
                                                                        shuffle=True,
                                                                        random_state=1004)

    evals = [(x_test, y_test)]
    val_evals = [(val_x_test, val_y_test)]
    #
    xgb_wrapper.fit(x_train, y_train, eval_set=evals, verbose=True)
    #
    val_xgb_wrapper.fit(val_x_train, val_y_train, eval_set=val_evals, verbose=True)

    preds = xgb_wrapper.predict(x_test)
    pred_prob = xgb_wrapper.predict_proba(x_test)[:, 1]

    val_preds = val_xgb_wrapper.predict(val_x_test)
    val_pred_prob = val_xgb_wrapper.predict_proba(val_x_test)[:, 1]

    # -----------------------결과-----------------------

    print('val_test')
    clf_eval.get_clf_eval(val_y_test, val_preds)
    feature_importance_plot.plot(xgb_wrapper)
    cross_val.score(xgb_wrapper, val_x_train, val_y_train)
    roc_curve_plot.roc_curve_plot(val_y_test, val_pred_prob)

    print('test')

    clf_eval.get_clf_eval(y_test, preds)
    feature_importance_plot.plot(xgb_wrapper)
    cross_val.score(xgb_wrapper, x_train, y_train)
    roc_curve_plot.roc_curve_plot(y_test, pred_prob)
