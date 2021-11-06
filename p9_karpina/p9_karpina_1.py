import numpy as np
import numpy.linalg
import itertools

while True:
        try:
            x = int(input("Put size of matrix: "))
            if x <= 0:
                print("Size can`t be negative or equal 0!")
                continue
            else:
                break
        except ValueError:
            print("Put a number!")
            continue

def random_matrix(dim):
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

matrix = random_matrix(x)
print(matrix)
print()

det = np.linalg.det(matrix)
dett = round(det)
print(f"Determinat is {det}")
print()

matrix_per = list(itertools.permutations(range(len(matrix)), len(matrix)))
print(np.matrix(matrix_per))
print()

signs = []
sign = 1
for i in range(len(matrix_per)):
    for j in matrix_per[i]:
        if i > j:
            sign *= -1
    signs.append(sign)
print(signs)