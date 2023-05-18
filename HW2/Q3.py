#!/usr/bin/python3
# HW2 _ Q3
"""
calculates sum of digits in a number until its less than 10
list of functions: sum_of_digits, main .
"""

def sum_of_digits(number: int) -> int:
    """
    gets an integer as argument and sums its digits while its
    bigger than 10 and returns the remaining one-digit integer.
    """
    while number > 10:
        x = sum(int(digit) for digit in str(number))
        number = x
    return x

## Code Hale Tamrin:
#def sum_digits(number: int) -> int:
#    summation = 0
#    while number > 0:
#        summation += number % 10
#        number //= 10
#    return number

def main():
    """
    a number will be passed to 'sum_of_digits' func.
    """
    number = 9876
    print("sum of digits of given number:",sum_of_digits(number))

if __name__ == "__main__":
    main()
