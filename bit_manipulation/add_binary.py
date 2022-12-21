class Solution:
    def addBinary(self, a, b):
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


s = Solution();

assert s.addBinary('111', '1111') == '10110'
assert s.addBinary('1', '1') == '10'
assert s.addBinary('0', '1') == '1'
assert s.addBinary('10111010100101', '1111100100000') == '100110111000101'
