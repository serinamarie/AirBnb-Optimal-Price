import pickle
import pandas as pd

def add_prediction(listing):
    """

    """
    # with open(ABB.pkl, 'rb') as file:
    #     pickle_model = pickle.load(file)
    # listing['price'] = 99
    columns = [x for x in listing]
    data = [listing[y] for y in columns]

    return data


