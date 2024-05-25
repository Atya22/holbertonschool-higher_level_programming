#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            end_char = " " if j != len(matrix[i]) - 1 else ""
            print("{:d}".format(matrix[i][j]), end=end_char)
        print()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
     ]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
