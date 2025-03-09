from typing import *

## load the stations from CSV file
def loadStations() -> Dict:
    stations = {};
    with open("assets/station_codes.csv", "r") as file:
        for line in file:
            line = line.strip().split(",");
            stations[line[0]] = line[1];
    return stations;

def resolveStation(station: str) -> str:
    stations = loadStations();
    ## search for the station by code and return the name
    for name, code in stations.items():
        if code == station.upper():
            return name;
    return "NOT FOUND";


