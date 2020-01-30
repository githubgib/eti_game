import time
import csv
menuList = ["Exit",
            "Read and load maze from file",
            "View maze",
            "Play maze game",
            "Configure current maze"]
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


# Menu while loop
while True:
    option = printMenu()

    if option is 1:
        print("Reading and loading maze from file...")
        filename = str(
            input("Enter the .csv file name (without .csv):"))+'.csv'
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(
                        f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
        time.sleep(1)
    elif option is 2:
        print("Viewing maze...")
        time.sleep(1)
    elif option is 3:
        print("Playing maze game...")
        time.sleep(1)
    elif option is 4:
        print("Configuring current maze...")
        time.sleep(1)
    elif option is 0:
        print("Shutting down...")
        time.sleep(2)
        print("Goodbye.")
        time.sleep(1)
        exit()
