# Given a string that may represent a number, determine if it is a number. Here's some of examples of how the 
# number may be presented:
# "123" # Integer
# "12.3" # Floating point
# "-123" # Negative numbers
# "-.3" # Negative floating point
# "1.5e5" # Scientific notation
# Here's some examples of what isn't a proper number:
# "12a" # No letters
# "1 2" # No space between numbers
# "1e1.2" # Exponent can only be an integer (positive or negative or 0)
# Scientific notation requires the first number to be less than 10, however to simplify the solution assume 
# the first number can be greater than 10. Do not parse the string with int() or any other python functions.

import re

def parse_number(s):
    # Chuck negative numbers
    if re.search('^-',s):
        s = s[1:]
    # If there is an e
    e = re.search('e',s)
    if e:
        # Make sure it is at the end followed by integers
        if not re.search('e[0-9]+$',s):
            return False
        # remove the e section
        else:
            s = s[:e.span()[0]] 
    
    # If just integers return true
    if re.search('^[0-9]+$',s):
        return True
    # If integers sperated by a single . then more integers return true
    elif re.search('^[0-9]*\.{1}[0-9]+$',s):
        return True
    else:
        return False
     
assert parse_number('12.3') == True, "12.3 is a number"
assert parse_number('-123') == True, "-123 is a number"
assert parse_number('-.3') == True, "-.3 is a number"
assert parse_number('5.5e5') == True, "5.5e5 is a number"
assert parse_number('1') == True, "1 is number"
assert parse_number('-4.0e4') == True, '-4.0e4 is a number'


assert parse_number('..') == False, '.. is not a number'
assert parse_number('--5') == False, '--5 is not a number'
assert parse_number('-4.0.0') == False, '-4.0.0 is not a number'




