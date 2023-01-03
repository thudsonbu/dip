class Solution:
    def myAtoi(self, s: str) -> int:
        # Clear whitespace and determine sign
        negative = False
        idx = 0

        # Skip beginning whitespace
        while idx < len(s) and s[idx] == ' ':
            idx += 1

        # Parse sign (if any)
        if idx < len(s) and s[idx] == '-':
            negative = True
            idx += 1
        elif idx < len(s) and s[idx] == '+':
            idx += 1

        # Read integers and add to return value
        output = 0
        while idx < len(s) and s[idx].isdigit():
            next_char = int(s[idx])
            output *= 10
            output += next_char
            idx += 1

        # Handle overflow
        if negative and output >= 2**31:
            output = 2**31
        elif output >= 2**31:
            output = 2**31 - 1

        # Handle sign
        if negative:
            return output * -1

        return output
