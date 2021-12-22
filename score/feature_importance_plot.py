import matplotlib.pyplot as plt
from xgboost import plot_importance

def plot(model):
    fig, ax = plt.subplots(figsize=(10, 12))

    plot_importance(model, ax=ax)
    plt.grid(True)
    plt.show()
