"""
Program Goals:
1. Get input from user (at multiple points)
2. We need to convert some of this input to INT"s from from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Returan a value to a specific index

"""
import random 
myList = []
uniqueList = []

def mainProgram():
    while True:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to a list or
2. Add a Bunch!
3. Return the value at an index position!
4. Random Search
5. Linear Seach
6. Sort List
7.  Recursive Binary Search
8.  Iterative Binary Search
9. Print Lists
10. Quit Program""")
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
                linearSearch()
            elif choice =="6":
                sortList(myList)
            elif choice =="7":
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice =="8":
                binSearch = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your umber is at index postion{}".format(result))
                else:
                    print("Your number is not found in that list!")
                    
            elif choice == "9":
                printLists()
            else:
                break
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

def sortList (myList):
    print("A little birdie told me you needed some sorted data!")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input ("Wanna see your new list?  Y/N")
    if showMe.lower() == "y":
        print(unique_list)

def randomSearch():
    print("RaNdOm SeArCh?!")
    print(myList[random.randint(0, len(myList)-1)])
    
def linearSearch():
    print("We're gonna check out each item one at a time in your list!")
    searchItem = input("What you lookin for, parder")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch (unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        
        if unique_list[mid] == x:
            print("Your number is at index postion {}".format(mid))
            return mid

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)

        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] <x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
                return mid
    return -1

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see, sorted or un-sorted?      ")
        if whichOne.lower() == "sorted":
                    print(unique_list)
        
                         
       
#dunder main
if __name__ == "__main__":
    mainProgram()
    
