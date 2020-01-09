import pickle
import pandas as pd
import numpy as np
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
    # del X_train["user_id"]
    del X_train["photo"]
    del X_train["title"]

    columns = ["summary","neighbourhood_cleansed","property_type","room_type","accommodates","bathrooms","cleaning_fee","minimum_nights","instant_bookable","kitchen","smoke_detector","self_check_in","hot_water"]
    data = np.array([X_train[y] for y in columns], ndmin=2)

    # df = pd.DataFrame(data,columns=columns)
    # X_test = df.iloc[0].values

    y_pred = pickle_model.predict(data)

    return str(X_test)