from sklearn import model_selection
def score(model,X,y):

    cross_score = model_selection.cross_val_score(model,X,y, cv=10)
    print(cross_score)
    print('cross score : ',cross_score.mean())