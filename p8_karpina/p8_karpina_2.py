import math

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
    
dis = (b**2)-(4*a*c)
print(f"The discriminant is {dis}")
try:
    if dis > 0:
        x1 = (-b + math.sqrt(dis))/(2*a)
        if 2*a == 0:
            raise ZeroDivisionError("Division by 0 is impossible!")
        else:
            print(f"The first root of eqation is {x1}")
        x2 = (-b - math.sqrt(dis))/(2*a)
        if 2*a == 0:
            raise ZeroDivisionError("Division by 0 is impossible!")
        else:
            print(f"The second root of eqation is {x2}")
    elif dis == 0:
        x = -b/2*a
        if 2*a == 0:
            raise ZeroDivisionError("Division by 0 is impossible!")
    else:
        print(f"Eqation doesn't have roots because discriminat {dis} is less than 0")
except ZeroDivisionError as zde:
    print(zde)