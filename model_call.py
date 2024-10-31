import requests
import json
from typing import Dict
import os

MODEL_URL = os.environ["model_url"]


def azure_model_rest_api_call(api_key: str, request_body: Dict):
    """
    Make an inference API call to a model hosted on Azure.

    Parameters:
    api_key (str): The API key for authorization.
    request_body (dict): Input data for the model inference.

    Returns:
    list: Predictions from the model (e.g., [0, 1]).
    """
    url = MODEL_URL

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    response = requests.post(url, headers=headers, json=request_body)

    return response.json()["predictedOutcomes"]
