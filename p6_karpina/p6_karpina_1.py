while True:
    phraze1 = set(filter(str.isalpha, input("Write your first phraze: ").lower()))
    phraze2 = set(filter(str.isalpha, input("Write your second phraze: ").lower()))
    letters = (phraze1 & phraze2)
    if phraze2.issubset(phraze1):
        print(phraze1)
        print(phraze2)
        print(letters)
        print("Letters from first phraze can be used in second phraze")
    else:
        print("Letters from first phraze can`t be used in second phraze")
    print("If you want stop the program press any key, if you want continue write `yes` ")  
    a = input()
    if a == "yes":
        continue
    else:
        print("Program has been stopped ")
        break