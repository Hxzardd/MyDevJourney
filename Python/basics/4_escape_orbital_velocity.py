G = 6.67*10**-11
M = float(input("Enter the mass: "))
r = float(input("Enter the radius: "))

V_o = ((G*M) / r)**(-1/2)

V_e = ((2*G*M) / r)**(-1/2)

print(f"The value of Orbital Velocity is: {V_o}\nThe value of Escape Velocity is: {V_e}")