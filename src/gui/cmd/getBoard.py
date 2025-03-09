from typing import *
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.font as tkFont

import src.api.getBoard as gB
import src.api.resolveStation as resolveStation

def getBoard():
    print("Get Board")
    ## get window from already open one
    window = tk.Toplevel()
    window.title("Departure.Town - Get Board")
    window.geometry("400x400")
    window.iconphoto(False, tk.PhotoImage(file="src/gui/icon.png"))

    ## add options
    tk.Label(window, text="Enter station code:").pack()
    station = tk.Entry(window)
    station.pack()

    tk.Label(window, text="Enter number of rows:").pack()
    rows = tk.Entry(window)
    rows.pack()

    tk.Button(window, text="Submit", command=lambda: submit(window, station.get(), rows.get())).pack()

    window.mainloop()

def submit(window: tk.Toplevel, station: str, rows: str) -> None:
    print(f"Station: {station} Rows: {rows}")
    ## display the data -- and make it look nice 
    ## also return an error if there is one e.g. WRONG CRS or something LIKE NO INTERNET

    ## 1-- check if the CRS is valid -- if not, return an error and make fun of the user from being so stupid
    if resolveStation.resolveStation(station) == "NOT FOUND":
        messagebox.showerror("Error", "Invalid CRS code.\nFeel free to try again, but don\'t expect a different result if you\'re still just as clueless.")
        window.destroy()
    else:
        ## get the data using CRS
        data = gB.getBoard(station, int(rows))

        if "error" in data.keys():
            messagebox.showerror("Error", data["error"])
            window.destroy()
        else:
            ## parse data
            # After fetching data:
            data = data["trainServices"]

            # Create the departure board window
            board_window = tk.Toplevel()
            board_window.iconphoto(False, tk.PhotoImage(file="src/gui/icon.png"))
            stationName = resolveStation.resolveStation(station)
            board_window.title(f"Departure.Town - {stationName}")

            # Configure the board window
            canvas = tk.Canvas(board_window)
            scrollbar = tk.Scrollbar(board_window, orient="horizontal", command=canvas.xview)
            scrollbar.pack(side="bottom", fill="x")
            canvas.pack(side="top", fill="both", expand=True)
            canvas.configure(xscrollcommand=scrollbar.set)

            # Frame to hold service columns
            main_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=main_frame, anchor="nw")

            # Styling
            bold_font = tkFont.Font(family="Courier New", size=12, weight="bold")
            normal_font = tkFont.Font(family="Courier New", size=12)

            # Process each service
            for service in data:
                try:
                    # Create a column for this service
                    service_column = tk.Frame(main_frame, borderwidth=1, relief="groove", padx=10)
                    service_column.pack(side="left", fill="y", expand=True)

                    # --- Destination ---
                    destination = (
                        service.get("destination", [{}])[0]  # Default to empty dict if missing
                        .get("locationName", "")
                    )
                    if destination:  # Only display if data exists
                        tk.Label(service_column, text=destination, font=bold_font).pack(anchor="w")

                    # --- STD ---
                    std = service.get("std", "")
                    if std:  # Only display if data exists
                        tk.Label(service_column, text=std, font=normal_font).pack(anchor="w")

                    # --- ETD ---
                    etd = service.get("etd", "")
                    if etd:  # Only display if data exists
                        tk.Label(service_column, text=etd, font=normal_font).pack(anchor="w")

                    # --- Platform ---
                    platform = service.get("platform", "")
                    if platform:  # Only display if data exists for the 4th time
                        tk.Label(service_column, text=f"Plat: {platform}", font=normal_font).pack(anchor="w")

                    # --- Calling At ---
                    calling_points = [
                        cp.get("locationName", "")
                        for sp in service.get("subsequentCallingPoints", [])  # Handle missing key
                        for cp in sp.get("callingPoint", [])  # Handle missing key
                    ]
                    calling_points = [cp for cp in calling_points if cp]  # Filter out empty strings
                    if calling_points:  # Only display if there are valid calling points
                        tk.Label(service_column, text="Calling at:", font=normal_font).pack(anchor="w")
                        for cp in calling_points:
                            tk.Label(service_column, text=f"    {cp}", font=normal_font).pack(anchor="w")

                except Exception as e:
                    print(f"Error processing service: {e}")
                    # Optionally add a placeholder column for failed services
                    tk.Label(main_frame, text="Service data unavailable", fg="red").pack(side="left")

            # Update canvas scrolling
            main_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            board_window.mainloop()