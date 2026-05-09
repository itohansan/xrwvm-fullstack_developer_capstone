
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    """Make GET request to the backend"""
    request_url = backend_url + endpoint
    try:
        response = requests.get(request_url, params=kwargs, timeout=10)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def analyze_review_sentiments(text):
    """Analyze sentiment of a review using sentiment analyzer service"""
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "neutral"}   # fallback


def post_review(data_dict):
    """Post a new review to the backend"""
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error posting review: {response.status_code}")
            return None
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None
