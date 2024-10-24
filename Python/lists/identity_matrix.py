n = int(input("Enter the size of the square matrix (n x n): "))

matrix = []
print("Enter the elements of the matrix row by row:")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input())
        row.append(element)
    matrix.append(row)

is_identity = True
for i in range(n):
    for j in range(n):
        if i == j:
            if matrix[i][j] != 1:
                is_identity = False
        else:
            if matrix[i][j] != 0:
                is_identity = False

if is_identity:
    print("The matrix is an identity matrix.")
else:
    print("The matrix is not an identity matrix.")
