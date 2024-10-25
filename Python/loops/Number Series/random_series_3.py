# S = 1 + x^2/2 + x^3/3 + ... + x^n/n

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
S = 1.0

for i in range(2, n + 1):
    S += (x ** i) / i

print(f"The sum of the series is {S:.2f}")
