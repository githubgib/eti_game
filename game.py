import time
import csv
import re
from termcolor import colored

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
completed = False
# Display Menu


def printMenu(menu):
    if menu == True:
        print(colored("\nMain Menu\n{}".format(bars), 'green'))
        for menu in range(1, 5):
            print(colored("[{}]{}{}".format(
                menu, '\t', menuList[menu]), 'green'))
        print('\n'*0)
        for m in range(0, 1):
            print(colored("[{}]{}{}".format(m, '\t', menuList[m]), 'green'))
        return "Menu displayed."
    else:
        return "Menu display error."


def mainMenu(option, cut=""):
    if option is 1:
        print("Reading and loading maze from file...")
        if cut == "cut":
            return "Reading maze."

        filename = str(
            input(colored("Enter filename (w/o .csv):", 'red')))+'.csv'
        try:
            checkFile(filename)
        except FileNotFoundError:
            print(colored("File wasn't found.", 'magenta'))
        return "Reading maze."

    elif option is 2:
        print("Viewing maze...")
        printMaze()
        return "Viewing maze."

    elif option is 3:
        print("Playing maze game...")
        if cut == "cut":
            return "Playing maze game."

        if len(maze) == 0:
            print(colored("The maze is empty. Please load one in from the menu.", 'blue'))
        else:
            playGame()

        return "Playing maze game."

    elif option is 4:
        print("Configuring current maze...")
        if cut == "cut":
            return "Configuring current maze."

        if len(maze) == 0:
            print(colored("The maze is empty. Please load one in from the menu.", 'blue'))
        else:
            ConfigureMenu()

        return "Configuring current maze."

    elif option is 0:
        print("Shutting down...")
        print("Goodbye.")
        return False

    else:
        print("You have entered an invalid option. Please re-enter your option.")
        return "Invalid option selected."


def checkFile(filename):
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

                print(f'Read {line_count} lines.')
        return line_count


def printConfigMenu():
    print("Configuration Menu\n{}".format(bars))
    for menu in range(1, 5):
        print("[{}]{}{}".format(menu, '\t', configMenuList[menu]))
    print('\n'*0)
    for m in range(0, 1):
        print("[{}]{}{}".format(m, '\t', configMenuList[m]))

    return(int(input(colored("Enter your option: ", 'red'))))


def ConfigureMenu():
    printMaze()
    configOption = printConfigMenu()
    if configOption is 0:
        pass
    elif configOption is 1:
        wallopt = str(input(colored(
            "Enter Coords Row,Column to add/replace with wall, or B(configure menu) or M(main menu) to return there:")))
        if wallopt is "B":
            ConfigureMenu()
        elif wallopt is "M":
            pass
        else:
            coords = [int(i) for i in wallopt.split(',')]
            print(coords)
            maze[coords[0]][coords[1]] = 'X'
    elif configOption is 2:
        passopt = str(input(colored(
            "Enter Coords Row,Column to add/replace with passageway, or B(configure menu) or M(main menu) to return there:", 'red')))
        if passopt is "B":
            ConfigureMenu()
        elif passopt is "M":
            pass
        else:
            coords = [int(i) for i in passopt.split(',')]
            print(coords)
            maze[coords[0]][coords[1]] = 'O'
    elif configOption is 3:
        startptopt = str(input(colored(
            "Enter Coords Row,Column to add/replace with start point, or B(configure menu) or M(main menu) to return there:", 'red')))
        if startptopt is "B":
            ConfigureMenu()
        elif startptopt is "M":
            pass
        else:
            coords = [int(i) for i in startptopt.split(',')]
            print(coords)
            maze[coords[0]][coords[1]] = 'A'
    elif configOption is 4:
        endptopt = str(input(colored(
            "Enter Coords Row,Column to add/replace with end point, or B(configure menu) or M(main menu) to return there:", 'red')))
        if endptopt is "B":
            ConfigureMenu()
        elif endptopt is "M":
            pass
        else:
            coords = [int(i) for i in endptopt.split(',')]
            print(coords)
            maze[coords[0]][coords[1]] = 'B'


# Returns start point of maze if it is found.
def searchStart():
    result = [(i, el.index("A"))
              for i, el in enumerate(maze) if "A" in el]
    if result == []:
        print("Maze doesn't have a start point!")
    else:
        print("Returning this value: %s", str(result[0]))
        return str(result[0])  # Converts to string so it is easier to pull


def validMove(coords, move):
    if move == 'up':
        if maze[coords[0]-1][coords[1]] == 'O' or maze[coords[0]-1][coords[1]] == 'B':
            return True
        else:
            return False
    if move == 'left':
        if maze[coords[0]][coords[1]-1] == 'O' or maze[coords[0]][coords[1]-1] == 'B':
            return True
        else:
            return False
    if move == 'down':
        if maze[coords[0]+1][coords[1]] == 'O' or maze[coords[0]+1][coords[1]] == 'B':
            return True
        else:
            return False
    if move == 'right':
        if maze[coords[0]][coords[1]+1] == 'O' or maze[coords[0]][coords[1]+1] == 'B':
            return True
        else:
            return False


def validCompletetion(coords, move):
    global completed
    if move == 'up':
        if maze[coords[0]-1][coords[1]] == 'B':
            completed = True
            return True
        else:
            return False
    if move == 'left':
        if maze[coords[0]][coords[1]-1] == 'B':
            completed = True
            return True
        else:
            return False
    if move == 'down':
        if maze[coords[0]+1][coords[1]] == 'B':
            completed = True
            return True
        else:
            return False
    if move == 'right':
        if maze[coords[0]][coords[1]+1] == 'B':
            completed = True
            return True
        else:
            return False


def movePlayer(direction):
    direction.upper()
    start_coords = searchStart()
    start_coords_formatted = re.split('[()]', start_coords)[1]

    if direction == 'W':
        # W - [-1, same index]
        coords = [int(i)
                  for i in start_coords_formatted.split(',')]

        if validCompletetion(coords, 'up'):
            print(colored("You've completed the maze. Good job!", 'magenta'))

        if validMove(coords, 'up'):
            maze[coords[0]][coords[1]] = 'O'
            maze[coords[0]-1][coords[1]] = 'A'
            printMaze()
            print(colored("Successfully moved up", 'green'))

        else:
            printInvalidOpt()

    elif direction == 'A':
        # A - [same index, -1]
        coords = [int(i)
                  for i in start_coords_formatted.split(',')]

        if validCompletetion(coords, 'left'):
            print(colored("You've completed the maze. Good job!", 'magenta'))

        if validMove(coords, 'left'):
            maze[coords[0]][coords[1]] = 'O'
            maze[coords[0]][coords[1]-1] = 'A'
            printMaze()
            print(colored("Successfully moved left", 'green'))

        else:
            printInvalidOpt()
    elif direction == 'S':
        # S - [+1, same index]
        coords = [int(i)
                  for i in start_coords_formatted.split(',')]
        if validCompletetion(coords, 'down'):
            print(colored("You've completed the maze. Good job!", 'magenta'))

        if validMove(coords, 'down'):
            maze[coords[0]][coords[1]] = 'O'
            maze[coords[0]+1][coords[1]] = 'A'
            printMaze()
            print(colored("Successfully moved down", 'green'))
        else:
            printInvalidOpt()
    elif direction == 'D':
        # D - [same, +1]
        coords = [int(i)
                  for i in start_coords_formatted.split(',')]

        if validCompletetion(coords, 'right'):
            print(colored("You've completed the maze. Good job!", 'magenta'))

        if validMove(coords, 'right'):
            maze[coords[0]][coords[1]] = 'O'
            maze[coords[0]][coords[1]+1] = 'A'
            printMaze()
            print(colored("Successfully moved right", 'green'))

        else:
            printInvalidOpt()
    else:
        print(colored(
            "That option is not a valid option. Please select another option", 'magenta'))


def printMaze():
    if len(maze) == 0:
        print(colored("The maze is empty. Please load one in from the menu.", 'blue'))
    else:
        print(colored(bars, 'blue'))
        for row in maze:
            for element in row:
                if element is "X":
                    print(colored(element, 'cyan'), end='')
                    print(" ", end="")
                if element is "A":
                    print(colored(element, 'red'), end='')
                    print(" ", end="")

                if element is "B":
                    print(colored(element, 'magenta'), end='')
                    print(" ", end="")

                if element is "O":
                    print(element, end='')
                    print(" ", end="")

            print("\n")
        # print(*maze, sep="\n")
        print(colored(bars, 'blue'))


def printInvalidOpt():
    print(colored(
        "That option is not a valid move. Please select another move", 'magenta'))


def playGame():
    global completed
    printMaze()
    while not completed:
        direction = str(input(
            colored("Enter move (WASD) or (M) to return. :", 'red'))).upper()
        if direction == "M":
            break
        elif direction in ["W", "A", "S", "D"]:
            movePlayer(direction)
        else:
            print("Invalid option.")

    # Menu while loop
if __name__ == "__main__":
    playing = True
    while (playing != False):
        try:
            printMenu(True)
            playing = mainMenu(
                int(input(colored("Enter your option: ", 'red'))))
        except ValueError:
            print("You have entered a digit range of 0 - 4. Please re-enter your option.")
            continue
