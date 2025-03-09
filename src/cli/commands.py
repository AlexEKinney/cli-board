### commands for the cli

from typing import *

def getBoard() -> Dict:
    from src.api.getBoard import getBoard
    station: str = input("Enter station code: ");
    rows: int = int(input("Enter number of rows: "));
    data = getBoard(station, rows);
    ## style the output (make it look nice) and return it
    ## parse it (JSON) 
    ## trainServices --> services --> service --> serviceID, std, etd, platform

    if "error" in data.keys():
        return data["error"];

    for service in data["trainServices"]:
        print(f"Service ID: {service['serviceID']}\nSTD: {service['std']}\nETD: {service['etd']}\nPlatform: {service['platform']}\n"); # basic output
# TODO: make it look nice, and not just dump useless data
