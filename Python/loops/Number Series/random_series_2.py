# Compute S = 1/2 + 3/4 + 5/6 + ....N terms


n = int(input())
s = 0
for i in range(0, n):
    num = (2 * i) + 1
    den = 2 * (i + 1)
    s += num/den
print(s)