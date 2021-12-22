import wrapper
import warnings
import set_data

warnings.filterwarnings('ignore')

x_train, x_test, y_train, y_test = set_data.data()
wrapper.Classifier(x_train, y_train, x_test, y_test)
