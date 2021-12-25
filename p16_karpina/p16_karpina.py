while True:
    try:
        n = int(input("Enter number of pages. Number of pages must be mulpitles of 16: "))
        if n > 1280:
            print("Please enter number of pages again")
        elif n <= 0:
            print("Please enter number of pages again")
        elif n % 16 != 0:
            print("Please enter numbers again. Pages must be multiples of 16")
        else:
            break
    except ValueError:
        print("Enter only numbers!")

def decorated(activate):
    def wrap(func):
        def wrapper(*args, **kwargs):
            book = func(*args, **kwargs)
            if activate:
                text_books = []
                for i in book:      
                    text_books.append([tuple(i[(4*j):(4*j+4)]) for j in range(4)])
                return text_books
            else:
                return book           
        return wrapper
    return wrap 

@decorated(activate=True) 
def pages(n):
    b = []
    num = int(n/16)
    for i in range(num):
        text_book = [16, 1, 2, 15, 14, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9]
        for j in range(16):
            text_book[j] += 16*i
        b.append(text_book)
    return b

print()
print(f"Total amount of notebooks in a book: {n/16}")
print()
print(f"Number of pages:")
for i in pages(n):
    print(i) 