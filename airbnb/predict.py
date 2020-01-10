import pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing

# import sys
# sys.path.append(r'path/to/python module file')

def add_prediction(listing):
    """

    """
    pkl_filename = "ABB.pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    # pickle_in = open("ABB.pkl", 'rb')
    # pickle_model = pickle.load(pickle_in)

    # listing['price'] = 99
    X_train = listing.copy()
    del X_train["id"]
    del X_train["user_id"]
    del X_train["photo"]
    del X_train["title"]
    del X_train["summary"]

    columns = ["host_response_rate","neighbourhood_cleansed","property_type","room_type","accommodates","bathrooms","cleaning_fee","minimum_nights","instant_bookable","kitchen","smoke_detector","self_check_in","hot_water","local_host"]
    data = [[X_train[y] for y in columns]]

    # f_names = pickle_model.feature_names
    # df = df[f_names]

    df = pd.DataFrame(data,columns=columns)
    df_2 = pd.get_dummies(df)
    # X_test = df.iloc[0].values

    y_pred = pickle_model.predict(df_2)
    # np.exp(y_pred)

    return str(y_pred)


    # {
# 	"photo": "https://picsum.photos/400/250?random=1578527625018",
# 	"title": "Whatever Dude",
# 	"summary": "This place is legiiiiiit",
# 	"host_response_rate": 100,
# 	"neighbourhood_cleansed": "Mitaka Shi",
# 	"property_type": "Hotel",
# 	"room_type": "Entire home/apt",
# 	"bathrooms": 3,
# 	"cleaning_fee": 33,
# 	"minimum_nights": 1,
# 	"instant_bookable": 0,
# 	"kitchen": 1,
# 	"smoke_detector": 0,
# 	"self_check_in": 1,
# 	"hot_water": 0,
# 	"accommodates":0,
# 	"id": 1578527625018,
# 	"room_type_Entire home/apt": 0,
# 	"property_type_Hotel": 0,
# 	"neighbourhood_cleansed_Mitaka Shi":0
# }