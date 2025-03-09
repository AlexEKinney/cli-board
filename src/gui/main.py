### GUI main file --> get user to choose option, then launch the corresponding function

import tkinter as tk

from typing import *

import src.api.manager as manager
import src.gui.cmd.getBoard as getBoard


def gui() -> None:
    ## init the window
    window = tk.Tk();
    window.title("Departure.Town - Python GUI");
    window.geometry("400x400"); ## arbitrary size -- means absolutely nothing but it looks quite funny
    window.resizable(False, False); ## DO NOT allow window to be resized!!!
    window.iconphoto(False, tk.PhotoImage(file="src/gui/icon.png"));


    tk.PhotoImage(file="src/gui/icon.png"); ## icon

    ## add options
    tk.Label(window, text="Choose an option:").pack();
    tk.Button(window, text="Get Board", command=getBoard.getBoard).pack();
    tk.Button(window, text="Set API Key", command=getBoard).pack();
    tk.Button(window, text="Exit", command=exitWindow).pack(); 
    ###

    window.mainloop();


def exitWindow() -> None:
    exit(0);
