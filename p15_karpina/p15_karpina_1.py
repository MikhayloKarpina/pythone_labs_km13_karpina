while True:
    try:
        n = int(input("Enter n: "))
        if n <= 0:
            print("Number can`t be less or equal 0")
            continue
        else:
            break
    except ValueError:
        print("Enter only number!")
        continue 

pascale = []

for i in range(n+1):
    r = [1] * (i + 1)
    for j in range(i+1):
        if j != 0 and j != i:
            r[j] = pascale[i - 1][j - 1] + pascale[i-1][j]
    pascale.append(r)

for i in pascale:
    print(i)