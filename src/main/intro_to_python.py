import numpy as np

def print_arr(m):
    for row in m:
        print(*row, sep=' ')
    print()


if __name__ == '__main__':
    # Size of square matrixs
    N = 3

    # Identity the matrix 
    m = np.identity(N, dtype=int)
    print_arr(m)

    # Add 3 to zero cells
    m[m == 0] += 3
    print_arr(m)

    # Excluding the last column
    m = m[:, :-1]
    print_arr(m)