rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the elements of matrix A:")
A = [[int(input()) for _ in range(cols)] for _ in range(rows)]

print("Enter the elements of matrix B:")
B = [[int(input()) for _ in range(cols)] for _ in range(rows)]

C_add = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

C_sub = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]

print("Matrix after addition:")
for row in C_add:
    print(" ".join(map(str, row)))

print("Matrix after subtraction:")
for row in C_sub:
    print(" ".join(map(str, row)))
