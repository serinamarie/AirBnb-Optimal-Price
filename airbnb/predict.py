import pickle

def add_prediction(listing):
    """

    """
    loaded_model = pickle.load(open(ABB.pkl, 'rb'))
    listing['price'] = 99

    return listing


