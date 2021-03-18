"""
Program Goals:
1. Get input from user (at multiple points)
2. We need to convert some of this input to INT"s from from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Returan a value to a specific index

"""
myList = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to a list or
2. Add a Bunch!
3. Return the value at an index position!
4. Random Search
5. Print contents of list
6. Quit Program""")
            #add a way to catch bad user responses
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice =="3":
                indexValues()
            elif choice =="4":
                randomSearch()
            elif choice =="5":
                print(myList)
            else:
                break
        except:
            print("You caught an error!")
        #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of repition

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a BUNCH of integers here!")
    numToAdd = input("How many integers would you like to add?           ")
    numRange = input ("And how high would you like these numbers to go?         ")
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print ("Your list is now complete.")

def indexValues():
    print("Ooooh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?")
    print (myList[int(indexPos)])

def randomSearch():
    print("RaNdOm SeArCh?!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSeach():
    print("We're gonna check out each item one at a time in your list!")
    searchItem = input("What you lokkin for, parder")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

#dunder main
if __name__ == "__main__":
    mainProgram()
    
