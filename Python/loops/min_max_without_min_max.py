N = int(input("Number of elements: "))
Num = []
for i in range(N):
    Num.append(int(input("Enter the elemdn: ")))
sorted_Num = sorted(Num)
print(sorted_Num[0])
print(sorted_Num[-1])