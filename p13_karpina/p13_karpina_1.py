counter = 0    
with open('gadsby.txt','r') as file:
    for line in file:
        for char in line:
            if char.isalpha():
                counter += 1

print(f"Gadsby have {counter} letters")

counter1 = {}
with open('gadsby.txt') as file:
    for line in file:
        for i in line.lower():
            if i.isalpha():
                if counter1.get(i):
                    counter1[i] +=  1 
                else:
                    counter1[i] = 1

for key in counter1:
    counter1[key] = (counter1[key] * 100)/counter
    counter1[key] = round(counter1[key], 3)
 
for i in reversed(sorted(counter1.items(), key=lambda para: para[1])):
    print(list(i))

print()
for i in range(5):
    print(list(reversed(sorted(counter1.items(), key=lambda para: para[1])))[i])
print()
for i in range(1,6):
    print(list(reversed(sorted(counter1.items(), key=lambda para: para[1])))[-i])