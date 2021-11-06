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

det = np.linalg.det(matrix)
print(round(det))

matrix_per = list(itertools.permutations(matrix))
for i in itertools.permutations(matrix):
    print(i)