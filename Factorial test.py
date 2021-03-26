def  factorial(x):

    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

if __name__ == "__main__":

    num = input("Waht do you want the factorial of?   ")
    print("The factorial of " , num , " is ", factorial(int(num)))
