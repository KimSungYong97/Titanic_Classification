from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

def data():
    dataset = pd.read_csv('./data/train.csv')
    print(dataset.head(5))

    x_features, y_label = Pretreatment(dataset)

    x_train, x_test, y_train, y_test = train_test_split(x_features, y_label, test_size=0.3, random_state=1004)
    print(x_train.shape, y_train.shape)

    return x_train, x_test, y_train, y_test


def Pretreatment(dataset):
    dataset['Sex'] = dataset['Sex'].map({'male': 0,
                                         'female': 1},
                                        na_action=None)

    dataset = pd.get_dummies(data=dataset, columns=['Embarked'], prefix='Embarked')
    dataset['Name'] = dataset['Name'].str.extract('([\w]+)\.', expand=False)
    dataset = pd.get_dummies(data=dataset, columns=['Name'], prefix='Name', dummy_na=True)
    dataset['Family']=dataset['SibSp']+dataset['Parch']

    dataset = dataset.drop(['Ticket', 'Cabin'], axis=1)
    print(dataset)

    return dataset.iloc[:, 2:], dataset.iloc[:, 1]
