Q_1 = float(input("Enter the value of first charge: "))
Q_2 = float(input("Enter the value of second charge: "))
r = float(input("Enter the value of radius: "))
k = 9*10**9

F = (k*Q_1*Q_2)/r**2

print(f"The value of the Force between the two charges is: {F}")