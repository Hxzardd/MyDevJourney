def sum_of_factors(n):
    total = 0
    i = 1
    while i < n:
        if n % i == 0:
            total += i
        i += 1
    return total

def are_amicable_numbers(a, b):
    return sum_of_factors(a) == b and sum_of_factors(b) == a

a = int(input())
b = int(input())
if are_amicable_numbers(a, b):
    print(f"{a} and {b} are Amicable numbers")
else:
    print(f"{a} and {b} are not Amicable numbers")
