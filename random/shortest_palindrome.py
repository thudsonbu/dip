# You are given a string s. You can convert s to palindrome by adding characters
# in front of it.

# Return the shortest palindrome you can find by performing this transformation.

# Intuition
# f(abcd): dcb + abcd = dcbabcd
# f(ba): a + ba = aba
# f(rhrer): re + rhrer = rerhrer


# Start with the last character in the string and add continue to add chars
# moving inward? For example, for the last of the above, start with r, check if
# it is a palindrome then add another?

# f(uebau):
#   uuebau
#   uauebau
#   uabuebau
#   uabeuebau

# Gonna give that a shot

class Solution:
    def shortestPalindrome(self, s):
        if len(s) < 2:
            return s

        prepend = ''

        idx = len(s) - 1
        while not self.checkPalindrome(prepend + s):
            prepend = prepend + s[idx]
            idx -= 1

        return prepend + s

    def checkPalindrome(self, s):
        mid = len(s) // 2

        l = s[0:mid][::-1]
        r = s[mid+(len(s) % 2):]

        return l == r
