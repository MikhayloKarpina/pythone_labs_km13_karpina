# Data validator
while True:
    try:
        eq = float(input("Write the strength of earthquake: "))
        if eq > 12:
            print("Max level of earquake is 12")
            continue
        elif eq < 0:
            print("Min level of earquake is 0")
            continue
    except ValueError:
        print("Write a number")
        continue
    # Data entry and inference block
    while True:
        if eq <= 3:
            print("It is weak earthquake")
        elif eq == 4:
            print("It is light earthquake")
        elif eq == 5:
            print("It is pretty strong earthquake")
        elif eq <= 7:
            print("It is strong earthquake")
        elif eq == 8:
            print("It is destructive earthquake")
        elif eq == 9:
            print("It is devastating earthquake")
        elif eq == 10:
            print("It is demolishing earthquake")
        elif eq <= 12:
            print("It is catastrophic earthquake")