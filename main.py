## main file --> get user to choose option, then launch the corresponding function

import src.cli.main as cli
import src.gui.main as gui
import src.api.resolveStation as resolveStation

choice = 0;

while(choice != 4):
    print(f"1. \"CLI\" Mode\n2. GUI Mode\n3. Export to CSV\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cli.cli();
    elif choice == 2:
        gui.gui();
    elif choice == 3:
        resolveStation.resolveStation(input("Enter station code: "));
    elif choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
