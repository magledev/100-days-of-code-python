# Simple program to check if a number is a prime number.


def prime_checker(number):
    is_prime = True
    for x in range(2, number - 1):
        if number % x == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
