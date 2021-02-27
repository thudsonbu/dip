# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given a number like 159 (non decimal), add the digits repeatedly until you get a single number.

# For instance, 1 + 5 + 9 = 15.
# 1 + 5 = 6.

# So the answer is 6.

class Solution(object):

    def add_digits_with_cast(self, num):
        #lets only deal with positives
        negative = False

        if num < 0:
            num = abs(num)
            negative = True

        num_str = str(num)
         
        # handle edge case
        if len(num_str) <= 1:
            return -num if negative else num
        
        while len(num_str) > 1:
            total = 0

            for char in num_str:
                total += int(char)
            
            num_str = str(total)

        return -int(num_str) if negative else int(num_str)

    def add_digits_without_cast(self, num):
        out = num

        while out // 10 > 0:
            total, magnitude = 0, 10

            while out > 0:
                total += out % magnitude
                out = out // magnitude

            out = total
        
        return out