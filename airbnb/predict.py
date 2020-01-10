import pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing

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
    data = [[X_train[y] for y in columns]]

    # f_names = pickle_model.feature_names
    # df = df[f_names]

    df = pd.DataFrame(daCta,columns=columns)
    df_2 = pd.get_dummies(df)
    # X_test = df.iloc[0].values

    y_pred = pickle_model.predict(df_2)

    return str(y_pred)