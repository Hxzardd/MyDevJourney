n = int(input())
s = 0
i = 1
while i < n:
    if n % i == 0:
        s += i
    i = i + 1
if s == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")