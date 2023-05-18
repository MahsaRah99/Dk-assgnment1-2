#!/usr/bin/python3
# HW2 _ Q2
"""
converts celsius unit to fahrenheit.
list of functions: 'celsius_2_fahrenheit', main .
"""

def celsius_2_fahrenheit(cel: float) -> float:
    """
    gets celsius unit as a float and returns fahrenheit unit in float.
    """
    fahr = cel * 1.8 + 32
    return fahr
     
def main():
    """
    a series of numbers will be passed to 'celsius_2_fahrenheit'
    func for conversion.
    """
    fahr_list = list(map(celsius_2_fahrenheit, (0,1,-32/1.8)))
    print("fahrenheit values of given celsius degrees: ",fahr_list)

if __name__ == "__main__":
    main()