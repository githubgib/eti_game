<<<<<<< HEAD
import time
menuList = ["Exit",
                        "Read and load maze from file",
                        "View maze",
                        "Play maze game",
                        "Configure current maze"]
bars = "="*35

#Display Menu
def printMenu():
    print("\nMain Menu\n{}".format(bars))
    for menu in range(1,5):
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
=======
def menu():
    print("THIS IS MY WORLD!")


menu()
>>>>>>> 94dd96218532529790471f96daf1ff35559f1407
