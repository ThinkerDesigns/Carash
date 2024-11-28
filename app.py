from flask import Flask, jsonify, request
import pandas as pd
import kaggle

# Test authentication and dataset download
kaggle.api.authenticate()  # This should authenticate you with the Kaggle API
kaggle.api.dataset_download_files('alexgude/california-traffic-collision-data-from-switrs', path='static/', unzip=True)

import os

app = Flask(__name__)

# Download the crash data from Kaggle (ensure you have your Kaggle API credentials set up)
def download_data():
    kaggle.api.dataset_download_files('alexgude/california-traffic-collision-data-from-switrs', path='static/', unzip=True)
    print("Dataset downloaded. Checking the folder contents...")
    return pd.read_csv('static/dataset.csv')


# Endpoint to fetch crash data
@app.route('/api/crash-data', methods=['GET'])
def get_crash_data():
    # Download dataset (replace with your Kaggle dataset)
    df = download_data()

    # Filter data based on search query (optional)
    query = request.args.get('query')
    if query:
        df = df[df['county_city_location'].str.contains(query, case=False, na=False)]

    # Convert to dictionary for JSON response
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
