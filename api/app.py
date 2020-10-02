from flask import Flask, request, jsonify
from .predict import add_prediction
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return 'airbnb predictive project'

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            # find authorization header
            listing = request.get_json(force=True)
            # content['predicted_price'] = 99
            content = jsonify(add_prediction(listing))
        except Exception as identifier:
            # content = {}
            content = str(identifier)
        return content
    
    return app

#  FLASK_APP=airbnb:APP FLASK_ENV=development flask run 

# def tokenize(text):
#     return [
#         token for token in simple_preprocess(text) if token not in STOPWORDS
#         ]
# @app.route('/', methods=['POST', 'GET'])
# def responses():
#     response = requests.get(
#         'backendurlhere')
#     return str(response.text)
# @app.route('/api', methods=['POST', 'GET'])
# def predict():
#     data = request.get_json(force=True)
#     desc = data['feature'][0]['description']
#     description_length = len(tokenize(desc))
