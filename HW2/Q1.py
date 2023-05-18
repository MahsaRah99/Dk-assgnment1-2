#!/usr/bin/python3
# HW2 _ Q1
"""
Searches for valid zip-codes in a list of strings.
list of functions: validating_pcode, main .
"""

import re

def validating_pcode(code_str: str) -> bool:
    """
    gets a string as an argument and returns True if the
    input has the defined pattern's format and False if 
    otherwise.
    """
    pattern = '^[0-9]{5}-[0-9]{5}$'
    result = re.match(pattern, code_str)
    if result:
        return True
    else:
        return False

    # Code Hale Tamrin:
#def is_valid_zipcode(zip_code: str) -> bool:
#    return(
#        isinstance(zip_code, str)
#        and len(zip_code) == 11
#        and zip_code[5] == '-'
#        and zip_code[:5].isdigit()
#        and zip_code[6:].isdigit()
#        )


def main():
    """
    'validating_pcode' function is called on a list of strings
    named codes_list, and filtered valid codes will be stored 
    in a list named correct_forms.
    """

    # codes_list = input("Enter postal codes separated by comma:").split(',')
    codes_list = ['12345-67890', '1234-09876', '1234567890',
    'Hi5','selff-five', '03452-12889']    
    
    correct_forms = list(filter(validating_pcode,codes_list))
    print("correct zip-codes are :",correct_forms)


if __name__ == "__main__":
    main()

