#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

def summation(num):

    sum = 0

    i = 1

    while i <= num:

        sum +=  i

        i +=  1

    return sum