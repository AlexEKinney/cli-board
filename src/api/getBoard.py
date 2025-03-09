### ext. --> get board
from typing import *
import requests
import json

from src.api.manager import baseURL, apiKey

def getBoard(station: str, rows: int) -> Dict:
    ## set headers for the request

    query: dict = {"numRows": rows};

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "insomnia/8.6.0",
        "x-apikey": apiKey
    }
    ## send req
    response = requests.request("GET", f"{baseURL}{station.upper()}", headers=headers, params=query);
    ## check status code
    if response.status_code == 200:
        return json.loads(response.text);
    else:
        return {"error": f"Error: {response.status_code}"};

