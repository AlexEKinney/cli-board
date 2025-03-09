import os
from typing import Dict
from dotenv import load_dotenv

# Load the .ENV file from the root of the project
def load_dotenv_file() -> None:
    if not load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.ENV')):
        raise FileNotFoundError("The .ENV file could not be loaded.\nDid you copy the .ENV.example, rename it to .ENV and add your API key?")

# Retrieve the API key from the environment variables
def getApiKey() -> str:
    api_key = os.getenv("APIKEY")
    if not api_key:
        raise ValueError("APIKEY not found in .ENV\nDid you add it?")
    return api_key

# Base URL for the API
baseURL: str = "https://api1.raildata.org.uk/1010-live-departure-board-dep/LDBWS/api/20220120/GetDepBoardWithDetails/" # Base URL for the API

# Load the environment variables when the script runs
load_dotenv_file()

# Set the API key from the environment
apiKey: str = getApiKey()

def setApiKey(key: str) -> None:
    global apiKey
    apiKey = key

def getApiKey() -> str:
    return apiKey

def getBaseURL() -> str:
    return baseURL
