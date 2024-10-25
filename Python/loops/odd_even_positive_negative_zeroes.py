# Read N and N number of integers in a list "Num". Count and display the number of odd, even, positive, negative integers and zeros.


N = int(input())
Num = []
for i in range(N):
    Num.append(int(input()))
odd = []
even = []
p = []
n = []
z = []
for num in Num:
    if num == 0:
        z.append(num)
    elif num > 0:
        if num % 2 == 0:
            p.append(num)
            even.append(num)
        else:
            odd.append(num)
    else:
        n.append(num)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
print(f"Odd numbers = {len(odd)}")
print(f"Even numbers = {len(even)}")
print(f"Positive numbers = {len(p)}")
print(f"Negative numbers = {len(n)}")
print(f"Zeroes = {len(z)}")