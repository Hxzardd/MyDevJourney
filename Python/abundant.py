r1 = int(input())
r2 = int(input())

n = r1
while n <= r2:
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i

    if s == n:
        print(f"{n} is a perfect number")
    elif s < n:
        print(f"{n} is a deficient number")
    else:
        print(f"{n} is a abundant number")
    n += 1