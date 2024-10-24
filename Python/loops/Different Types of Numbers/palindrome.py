n = int(input())
n_copy = n
s = 0
while n > 0:
    d = n % 10
    s = s * 10 + d
    n = n // 10
if s == n_copy:
    print(f"Given number {n_copy} is a palindrome number.")
else:
    print(f"Given number {n_copy} is not a palindrome number.")