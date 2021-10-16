numbers = {
    '1': ['.', '?','!', ':'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [' ']}
while True:
    message = input("Write your message: ").lower()
    code = ""
    for i in message:
        for j in numbers:
            try:
                code += (numbers[j].index(i) + 1) * j + ' '
            except ValueError:
                continue
    print(f"Your code is {code.strip()}")   
    print("If you want stop the program press any key, if you want continue write `yes` ")  
    a = input()
    if a == "yes":
        continue
    else:
        print("Program has been stopped ")
        break