import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv("sentiment_analyzer_url", default="http://localhost:5050/")


# GET request to backend with optional query parameters
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "&".join(f"{key}={value}" for key, value in kwargs.items())

    request_url = f"{backend_url}{endpoint}"
    if params:
        request_url += f"?{params}"

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")


# GET request to sentiment analyzer for analyzing review text
def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected error: {err}, type: {type(err)}")
        print("Network exception occurred")


# POST request to backend for inserting a review
def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
