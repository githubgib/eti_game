import time
import csv
maze = []
menuList = ["Exit",
            "Read and load maze from file",
            "View maze",
            "Play maze game",
            "Configure current maze"]
configMenuList = [
    "Exit to Main Menu",
    "Create Wall",
    "Create Passageway",
    "Create start point",
    "Create end point",
]
bars = "="*35

# Display Menu


def printMenu():
    print("\nMain Menu\n{}".format(bars))
    for menu in range(1, 5):
        print("[{}]{}{}".format(menu, '\t', menuList[menu]))
    print('\n'*0)
    for m in range(0, 1):
        print("[{}]{}{}".format(m, '\t', menuList[m]))

    return(int(input("Enter your option: ")))


def printConfigMenu():
    print("Configuration Menu\n{}".format(bars))
    for menu in range(1, 5):
        print("[{}]{}{}".format(menu, '\t', configMenuList[menu]))
    print('\n'*0)
    for m in range(0, 1):
        print("[{}]{}{}".format(m, '\t', configMenuList[m]))

    return(int(input("Enter your option: ")))


def ConfigureMenu():
    print(*maze, sep="\n")
    configOption = printConfigMenu()
    if configOption is 0:
        # return to menu
        pass
    elif configOption is 1:
        # create a wall
        wallopt = str(input(
            "Coords (Row,Column) to configure, or B(configure menu) or M(main menu) to return there:"))
        if wallopt is "B":
            ConfigureMenu()
        elif wallopt is "M":
            pass  # returns to main menu

    elif configOption is 2:
        # create passageway
        pass
    elif configOption is 3:
        # create start point
        pass
    elif configOption is 4:
        # create end point
        pass
    time.sleep(1)


# Menu while loop
while True:
    option = printMenu()

    if option is 1:
        print("Reading and loading maze from file...")
        filename = str(
            input("Enter the .csv file name (without .csv):"))+'.csv'
        # Read the maze file here
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    maze.insert(0, row)
                    line_count += 1
                    print(row)
                elif line_count == 1:
                    maze.insert(1, row)
                    line_count += 1

                elif line_count == 2:
                    maze.insert(2, row)
                    line_count += 1

                elif line_count == 3:
                    maze.insert(3, row)
                    line_count += 1

                elif line_count == 4:
                    maze.insert(4, row)
                    line_count += 1

                elif line_count == 5:
                    maze.insert(5, row)
                    line_count += 1

                elif line_count == 6:
                    maze.insert(6, row)
                    line_count += 1

                elif line_count == 7:
                    maze.insert(7, row)
                    line_count += 1

                # Remove comment to print maze array for debug
                # print(f"Final Maze array {maze}")
                print(f'Read {line_count} lines.')
        time.sleep(1)
    elif option is 2:
        print("Viewing maze...")
        # Prints the arrays, seperated with a new line for proper formatting.
        print(*maze, sep="\n")
        time.sleep(1)
    elif option is 3:
        print("Playing maze game...")
        time.sleep(1)
    elif option is 4:
        ConfigureMenu()
    elif option is 0:
        print("Shutting down...")
        time.sleep(2)
        print("Goodbye.")
        time.sleep(1)
        exit()
