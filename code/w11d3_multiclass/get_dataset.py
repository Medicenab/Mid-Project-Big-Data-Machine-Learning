from sklearn.datasets import fetch_openml

def get_sample_dataset():
    X,y = fetch_openml("mnist_784", version=1,return_X_y=True)

    # Extraemos solo las 20000 primeras imagenes del dataset, para trabajar con menos datos
    return  X[:20000], y[:20000]