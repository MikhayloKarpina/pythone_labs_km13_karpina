def dec_to_hex(number: int):
    table = '0123456789ABCDEF'
    result = ''
    while number:
        number, mod = number // 16, number % 16
        result = table[mod]+result
    return result

while True:
    color1 = int(input("Write first number of your color in range [0;255]: "))
    if 0 <= color1 <= 255:
        break
    print("Number can't be more than 255 and less than 0!")
while True:
    color2 = int(input("Write first number of your color in range [0;255]: "))
    if 0 <= color2 <= 255:
        break
    print("Number can't be more than 255 and less than 0!")
while True:
    color3 = int(input("Write first number of your color in range [0;255]: "))
    if 0 <= color3 <= 255:
        break
    print("Number can't be more than 255 and less than 0!")

print(end = '')
for i in color1, color2, color3:
    print(dec_to_hex(i), end = '')

print()