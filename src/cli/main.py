### MAIN cli entry point
from typing import *

from src.api.manager import setApiKey
from src.cli.commands import *

## list of commands
## imported from commands.py

commands = {
    "getBoard": getBoard,
    "setAPIKey": setApiKey
};

def cli() -> None:
    print("CLI Mode");
    print("Available commands:");
    for key in commands.keys():
        print(f"\t{key}");
    command: str = input("Enter command: ");
    ## number --> command --> commands --> run function
    ## now check index to make sure that number entered is in teh command list
    if command in commands.keys():
        res = commands[command](); ## run the command
        print(res); ## print the result
    else:
        print("Invalid command. Please try again.");
