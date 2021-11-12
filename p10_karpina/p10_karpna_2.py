import numpy as np

years = np.arange(1900, 2020+1, 1)


interclary_years = list(filter(lambda i: (i % 4 == 0 and i % 100 != 0) or i % 400 == 0, years))
print(f"Interclary years are: {interclary_years}")

while True:
    try:
        year = int(input("Enter any interclary year: "))
        if year in interclary_years:
            break
        else:
            print("Enter only inteclary year")
            continue
    except ValueError:
        print("Enter a number!")
        continue

while True:
    try:
        month = int(input("Enter any mount: "))
        if month < 1 or month > 12:
            print("We have only 12 mouth in year")
            continue
        else:
            break
    except ValueError:
        print("Enter a number!")
        continue

months = {1 : "january and it has 31 days in month",
          2 : "febuary and it has 29 days in month",
          3 : "march and it has 31 days in month",
          4 : "april and it has 30 days in month",
          5 : "may and it has 31 days in month",
          6 : "june and it has 30 days in month",
          7 : "july and it has 31 days in month",
          8 : "august and it has 31 days in month",
          9 : "september and it has 30 days in mont",
          10 : "october and it has 31 days in month",
          11 : "november and it has 30 days in month",
          12 : "december and it has 31 days in month"}

if month in months.keys():
    print(f"Your month is {months[month]}")