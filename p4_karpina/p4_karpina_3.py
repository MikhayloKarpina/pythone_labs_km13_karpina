while True:
    try:
        time = float(input("Write how long did you talk on the phone during this mounth: "))
        if time < 0:
            print("Time can not be smaller than 0")
            continue
    except ValueError:
        print("Write a number")
    while True:
        if time <= 50:
            print("You have to pay 100 grn")
            break
        elif time <= 100:
            print("You Have to pay 150 grn")
            break
        if time >= 100:
            money = 150+(time-100)*2
            print(money)
            break