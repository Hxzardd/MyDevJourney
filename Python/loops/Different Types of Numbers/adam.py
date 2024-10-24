def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def is_adam_number(n):
    n_square = n * n
    reverse_n = reverse_number(n)
    reverse_n_square = reverse_n * reverse_n
    return reverse_number(n_square) == reverse_n_square

n = int(input())
if is_adam_number(n):
    print(f"{n} is an Adam number")
else:
    print(f"{n} is not an Adam number")