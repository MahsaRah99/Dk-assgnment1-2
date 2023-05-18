#!/usr/bin/python3
# HW2 _ Q4
"""
calculates neper number using taylor's expansion.
list of functions: factorial, power, neper_exp, main .
"""


def factorial(n: int) -> int:
    """
    gets an integer argument and returns its factorial.
    """
    result = 1
    for i in range(2,n+1):
        result *= i

    return result

def power(num: int | float, pow: int) -> int | float:
    """
    gets 2 arguments, num and pow,and returns the value of num
    to the power of pow.
    """
    result = 1
    for _ in range(pow):
        result *= num

    return result


def neper_exp(x: int, n: int) -> float:
    """
    calculates neper number using factorial and pow functions. 
    gets 2 int arguments x and n wich are power of e and poly-
    nomial's degree respectively.
    """
    exp = 0
    for i in range(n):
        exp += power(x,i)/factorial(i)

    return f'{exp:.3f}'

def main():
    
    print("e expansion is equal to: ",neper_exp(1,8))
    print("e^2 expansion is equal to: ",neper_exp(2,7))

if __name__ == "__main__":
    main()