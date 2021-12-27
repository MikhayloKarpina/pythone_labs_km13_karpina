import factorial
import exp_root
import logaritm

def main():
    while True:
        try:
            n = int(input("\nEnter number: "))
            if n == int(n):
                break
        except ValueError:
            print("Enter only numbers!")
            continue

    while True:
        try:
            print("\nEnter '1' to use factorial \nEnter '2' to use exponential and root \nEnter '3' to use logaritm")
            choice = int(input("\nEnter what you want to use: "))
            if choice == 1:
                if n >= 0:
                    print(f"\nFactorial of your number is {factorial.fact(n)}\n")
                    break
                else:
                    print("Sorry, but factorial of negative number doesn't exist\n")
                    break
            elif choice == 2:
                print(f"\nSquare of your number is {exp_root.exp1(n)}")
                print(f"Cube of your number is {exp_root.exp2(n)}")
                print(f"Cube root of your number is {exp_root.root2(n)}")
                if n > 0:  
                    print(f"Square root of your number is {exp_root.root1(n)}\n")
                    break
                else:
                    print("Sorry, but you entered negatine number, so we can't find square root\n")
                    break
            elif choice == 3:
                while True:
                    try:
                        a = int(input("\nEnter base of logaritm: "))
                        if a <= 1:
                            print("Base can't be negative or equal 0 or 1")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Enter only numbers!")
                        continue
                print(f"\nLogaritm with base {a} of your number is {logaritm.log(n,a)}")
                print(f"Natural logaritm of your number is {logaritm.ln(n)}")
                print(f"Logaritm with base 10 of your number is {logaritm.lg(n)}\n")
                break
            else:
                print("Enter only 1, 2 or 3!")
        except ValueError:
            print("Enter only numbers!")
            continue

if __name__ == "__main__":
    main()