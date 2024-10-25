# Read N and N number of integers in a list "Num". Display the number of occurrences of each integer.

N = int(input("Number of elements: "))
a = []
d = []
for i in range(N):
    t = int(input("Enter the element: "))
    a.append(t)
for i in a:
    if i not in d:
        d.append(i)
for i in d:
    print(f"{i} occurs {a.count(i)} time(s)")