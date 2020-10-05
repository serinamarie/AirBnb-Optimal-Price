#  FLASK_APP=airbnb:APP FLASK_ENV=development flask run
from flask import Flask, request, jsonify
from .predict import find_price
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return 'Tokyo Airbnb Price Appraisal Tool'

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            listing = request.get_json(force=True)
            content = jsonify(find_price(listing))
        except Exception as identifier:
            content = {"error": str(identifier)}
        return content

    return app
