import math

# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-231, 231 - 1], then return 0. Assume that the environment does not allow you
# to store 64 bit integers (signed or unsigned).

class Solution:
    def reverse(self, x):
        magnitude = 10
        output = 0

        max_signed_int = 2**31

        negative = True if x < 0 else False

        if negative:
            x *= -1

        while x != 0:
            remainder = x % magnitude

            x -= remainder
            digit = math.floor(remainder / (magnitude / 10))

            if output > math.floor(max_signed_int/10):
                return 0
            elif output == math.floor(max_signed_int/10) and digit > max_signed_int % 10:
                return 0

            output *= 10
            output += digit

            magnitude *= 10

        if negative:
            return output * -1

        return output
