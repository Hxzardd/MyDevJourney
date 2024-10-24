L = float(input("Enter the Inductance: "))
i = float(input("Enter the Current: "))

U = (L*i**2) / 2

print(f"The value of energy stored in the inductor is: {U}")