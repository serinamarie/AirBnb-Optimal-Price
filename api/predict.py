import pickle
import pandas as pd
import numpy as np
from pathlib import Path
import json


def find_price(listing):
    path_to_file = Path("./notebooks/final_model.pkl")
    with open(path_to_file, 'rb') as file:
        pickle_model = pickle.load(file)

    features = listing.copy()
    columns = ["host_response_rate", "neighbourhood_cleansed", "property_type", "room_type", "accommodates", "bathrooms",
               "cleaning_fee", "minimum_nights", "instant_bookable", "kitchen", "smoke_detector", "self_check_in", "hot_water", "local_host"]

    data = [[features[col_name] for col_name in columns]]
    df = pd.DataFrame(data, columns=columns)

    replaced_room_type = {'Entire home/apt': 0,
                          'Private room': 1, 'Hotel room': 2, 'Shared room': 3}
    df['room_type'] = df['room_type'].map(replaced_room_type)

    replaced_neighbourhood_cleansed = {
        'Sumida Ku': 0, 'Hino Shi': 1, 'Chuo Ku': 2}
    df['neighbourhood_cleansed'] = df['neighbourhood_cleansed'].map(
        replaced_neighbourhood_cleansed).fillna(3)

    replaced_property_type = {'Apartment': 0,
                               'House': 1, 'Hostel': 2, 'Hotel': 3}
    df['property_type'] = df['property_type'].map(
        replaced_property_type).fillna(4)

    y_pred = pickle_model.predict(df)
    y_pred = np.exp(y_pred)
    prediction = {'predicted_price': int(y_pred)}

    return prediction
