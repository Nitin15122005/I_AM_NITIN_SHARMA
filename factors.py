def print_factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

number = int(input("Enter a number : "))

print_factors(number)