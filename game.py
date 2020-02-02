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


def printMenu(menu):
    if menu == True:
        print("\nMain Menu\n{}".format(bars))
        for menu in range(1, 5):
            print("[{}]{}{}".format(menu, '\t', menuList[menu]))
        print('\n'*0)
        for m in range(0, 1):
            print("[{}]{}{}".format(m, '\t', menuList[m]))
        return "Menu displayed."
    else:
        return "Menu display error."
    # return(int(input("Enter your option: ")))

def mainMenu(option, cut = ""):
    if option is 1:
        print("Reading and loading maze from file...")
        time.sleep(1)
        if cut == "cut":
            return "Reading maze."
        
        filename = str(input("Enter the .csv file name (without .csv):"))+'.csv'
        checkFile(filename)
        return "Reading maze."


    elif option is 2:
        print("Viewing maze...")
        time.sleep(1)
        # Prints the arrays, seperated with a new line for proper formatting.
        print(*maze, sep="\n")
        return "Viewing maze."

    elif option is 3:
        print("Playing maze game...")
        time.sleep(1)

        # loop through the entire maze array
        # find the starting point (A)
        # ask user for input (WASD - up left, down right, M for return to menu) validation stop

        # W - [-1, same index]
        # A - [same index, -1]
        # S - [+1, same index]
        # D - [same, +1]

        # alter array accordingly
        # check if the input is valid, is it O?
        # if the input move is valid,
        # replace starting coords with O
        return "Playing maze game."

    elif option is 4:
        print("Configuring current maze...")
        time.sleep(1)
        if cut == "cut":
            return "Configuring current maze."
        ConfigureMenu()
        return "Configuring current maze."
        

    elif option is 0:
        print("Shutting down...")
        time.sleep(2)
        print("Goodbye.")
        time.sleep(1)
        return False

    else:
        print("You have entered an invalid option. Please re-enter your option.")
        return "Invalid option selected."

def checkFile(filename):
    # Read the maze file here
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                maze.insert(0, row)
                line_count += 1
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
        return line_count

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
            "Enter Coords Row,Column to add/replace with wall, or B(configure menu) or M(main menu) to return there:"))
        if wallopt is "B":
            ConfigureMenu()  # returns to confgiure menu
        elif wallopt is "M":
            pass  # returns to main menu
        else:
            coords = [int(i) for i in wallopt.split(',')]  # eg: [0,1]
            print(coords)
            maze[coords[0]][coords[1]] = 'X'  # insert X at maze[row][column]
    elif configOption is 2:
        # create passageway
        passopt = str(input(
            "Enter Coords Row,Column to add/replace with passageway, or B(configure menu) or M(main menu) to return there:"))
        if passopt is "B":
            ConfigureMenu()  # returns to confgiure menu
        elif passopt is "M":
            pass  # returns to main menu
        else:
            coords = [int(i) for i in passopt.split(',')]  # eg: [0,1]
            print(coords)
            maze[coords[0]][coords[1]] = 'O'  # insert O at maze[row][column]
    elif configOption is 3:
        # create start point
        startptopt = str(input(
            "Enter Coords Row,Column to add/replace with start point, or B(configure menu) or M(main menu) to return there:"))
        if startptopt is "B":
            ConfigureMenu()  # returns to confgiure menu
        elif startptopt is "M":
            pass  # returns to main menu
        else:
            coords = [int(i) for i in startptopt.split(',')]  # eg: [0,1]
            print(coords)
            maze[coords[0]][coords[1]] = 'A'  # insert B at maze[row][column]
    elif configOption is 4:
        # create end point
        endptopt = str(input(
            "Enter Coords Row,Column to add/replace with end point, or B(configure menu) or M(main menu) to return there:"))
        if endptopt is "B":
            ConfigureMenu()  # returns to confgiure menu
        elif endptopt is "M":
            pass  # returns to main menu
        else:
            coords = [int(i) for i in endptopt.split(',')]  # eg: [0,1]
            print(coords)
            maze[coords[0]][coords[1]] = 'B'  # insert B at maze[row][column]


# Menu while loop
if __name__ == "__main__":
    playing = True
    while (playing != False):
        printMenu(True)
        playing = mainMenu(int(input("Enter your option: ")))
