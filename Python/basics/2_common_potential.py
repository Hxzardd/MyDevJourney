C_1 = float(input("Please enter the value of first capacitor: "))
C_2 = float(input("Please enter the value of second capacitor: "))
V_1 = float(input("Please enter the value of first potential source: "))
V_2 = float(input("Please enter the value of second potential source: "))

V_c = (C_1*V_1 + C_2*V_2) / (C_1 + C_2)

print(f"The value of common potential is: {V_c}")