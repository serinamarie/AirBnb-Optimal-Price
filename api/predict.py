import pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing

# import sys
# sys.path.append(r'path/to/python module file')

def add_prediction(listing):
    pkl_filename = "final_model.pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    X_train = listing.copy()
    del X_train["id"]
    del X_train["user_id"]
    del X_train["photo"]
    del X_train["title"]
    del X_train["summary"]

    columns = ["host_response_rate","neighbourhood_cleansed","property_type","room_type","accommodates","bathrooms","cleaning_fee","minimum_nights","instant_bookable","kitchen","smoke_detector","self_check_in","hot_water","local_host"]
    data = [[X_train[y] for y in columns]]

    df = pd.DataFrame(data,columns=columns)

    replaced_room_type = {'Entire home/apt': 0 , 'Private room': 1 , 'Hotel room':2,'Shared room':3 }
    df['room_type']= df['room_type'].map(replaced_room_type)
    
    replaced_neighbourhood_cleansed = {'Sumida Ku': 0 , 'Hino Shi': 1 , 'Chuo Ku':2}
    df['neighbourhood_cleansed']= df['neighbourhood_cleansed'].map(replaced_neighbourhood_cleansed).fillna(3)

    replaced_apartment_type = {'Apartment': 0 , 'House': 1 , 'Hostel':2, 'Hotel':3}
    df['property_type']= df['property_type'].map(replaced_apartment_type).fillna(4)

    y_pred = pickle_model.predict(df)
    y_pred = np.exp(y_pred)

    listing['predicted_price'] = y_pred[0]
    return str(listing)