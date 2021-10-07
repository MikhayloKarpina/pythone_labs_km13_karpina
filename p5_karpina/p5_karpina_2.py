while True:
    words = input("Write what ever you want searated by a space: ")
    words = list(words.split())
    long = len(words)
    if long == 1:
        print(words[0])
    else:
        comma = ",".join(words[:-1])
        last_word = words[-1]
        output = " and ".join([comma,last_word])
        print(output)
    print("If you want stop the program press any key, if you want continue write `yes` ")  
    a = input()
    if a == "yes":
        continue
    else:
        print("Program has been stopped ")
        break