"""
Program Goals:
1. Get input from user (at multiple points)
2. We need to convert some of this input to INT"s from from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Returan a value to a specific index

"""
import random
import time
myList = []
uniqueList = []


def mainProgram():
    while True:
        try:
            print ("Hey Let's Work With Listsssss!!!!!!")
            time.sleep(1)
            startList = input("Would you like a step-by-step help?  Y/N   ")
            if startList == "y":
                print("Cool! So with this we will walk through some basic functions like adding single and tons of integers to lists!")
                time.sleep(2.5)
                print("First we will just add one integer!")
                time.sleep(1.5)
            newItem = input("Type an integer here!    ")
            myList.append(int(newItem))

            print ("Awesome!")
            addAlot = input("Would You like to continue with help? Y/N      ")
            if addAlot == "y":                 
                print ("We will now add alot of integers! First we'll set a range and how many you wanna add!")
                time.sleep(2)
                numToAdd = input("How Many Integers Would You Like to Add?  ")
                numRange = input("And How High Would You Like These Numbers To Go?  ")
                for x in range(0,int(numToAdd)):
                    myList.append(random.randint(0, int(numRange)))
                print("Your List is Now Complete!")
                time.sleep(1.8)
                print("Now you have completed a list!")
                time.sleep(0.5)
                seeList = input("Would you like to see that list?   Y/N       ")
                if seeList == "y":
                    printLists()
                print("Now try to use these other functions!")
                    
                
        

            choice = input("""1. Add a Bunch!
2. Return The Value at an Index Position
3. Random Search
4. Linear Search
5. Sort List
6. Print Lists
7. Recursive Binary Search
8. Iterative Binary Search
9. Quit Program""")
            if choice == "1":
                addABunch()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                randomSearch()
            elif choice == "4":
                linearSearch()
            elif choice == "5":
                sortList(myList)
            elif choice == "6":
                printLists()
            elif choice == "7":
                binSearch = input("What number are you looking for?        ")
                recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?       ")
                result = iterativeBinarySearch(uniqueList, int(binSearch))
            if result != -1:
                print("Your number is at index position {}".format(result))
            else:
                print("Your number is not found in that list!")
                break
        except:
                print("Loser")

       
def addABunch():
    print("We're Gonna Add a Bunch of Integers Here!")
    numToAdd = input("How Many Integers Would You Like to Add?  ")
    numRange = input("And How High Would You Like These Numbers To Go?  ")
    for x in range(0,int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your List is Now Complete.")
   

def indexValues():
    print("I Heard You Needed Some Data!")
    indexPos = input("What index position are you curious about?        ")
    print (myList[int(indexPos)])

def sortList (myList):
    print("A little birdie told me you needed some sorted data!        ")
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showMe = input("Wanna see your new list?   Y/N")
    if showMe.lower() == "y":
        print(uniqueList)
   
def randomSearch():
    print("RaNdOm SeArCh?!")
    print(myList[random.randint(0,len(myList)-1)])
    if len(uniqueList) > 0:
        print(uniqueList[random.randint(0, len(uniqueList)-1)])

def linearSearch():
    print("We're Gonna Check Out Each Item One at a Time In Your List! This Sucks.")
    searchItem = input("What you looking for, pardner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqueList[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid
       
        elif uniqueList[mid] > x:
            return recursiveBinarySearch(uniqueList, low, mid - 1, x)
       
        else:
            return recursiveBinarySearch(uniqueList, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        whichOne = input("Which list? sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(uniqueList)
        else:
            print(myList)

def iterativeBinarySearch(uniqueList, x):
    low = 0
    high = len(uniqueList)-1
    mid = 0

    while low <= high:
        mid = (High + low) // 2

        if uniqueList[mid] < x:
            low = mid + 1

        elif uniqueList[mid] > x:
            high - mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    mainProgram()


