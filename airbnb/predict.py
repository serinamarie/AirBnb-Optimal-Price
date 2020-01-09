import pickle
import pandas as pd
# import sys
# sys.path.append(r'path/to/python module file')

def add_prediction(listing):
    """

    """
    # pkl_filename = "ABB.pkl"
    # with open(pkl_filename, 'rb') as file:
    #     pickle_model = pickle.load(file)

    pickle_in = open("ABB.pkl", 'rb')
    pickle_model = pickle.load(pickle_in)

    # listing['price'] = 99
    X_train = listing.copy()
    del X_train["id"]
    del X_train["photo"]

    columns = [x for x in X_train]
    data = [[X_train[y] for y in columns]]

    df = pd.DataFrame(data,columns=columns)
    X_test = df.iloc[0]

    # y_pred = pickle_model.predict(X_test)

    return str(X_test)


