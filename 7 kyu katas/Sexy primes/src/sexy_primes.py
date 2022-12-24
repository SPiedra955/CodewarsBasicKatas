#Sexy primes are pairs of two primes that are 6 apart. In this kata, your job is 
#to complete the function which returns true if x & y are sexy, false otherwise.

def is_prime(num):

    divisor = 2

    while divisor < num and num % divisor != 0:
        divisor += 1

    if divisor == num:
        return True
    return False


def sexy_prime(x, y):

    return is_prime(x) and is_prime(y) and (x - y == 6 or y - x == 6)
