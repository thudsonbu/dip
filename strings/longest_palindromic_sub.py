import math


def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    start = 0
    end = 0

    for i in range(0, len(s) - 1):
        mLen = max(expandAround(s, i, i), expandAround(s, i, i + 1))

        if mLen > (end - start):
            end = i + math.ceil(mLen / 2)
            start = i - math.floor(mLen / 2)

    return s[start:end+1]


def expandAround(s: str, left: int, right: int) -> int:
    start = 0
    end = 0

    while s[left] == s[right]:
        start = left
        end = right

        if left == 0:
            break

        if right == len(s) - 1:
            break

        left -= 1
        right += 1

    return end - start


print(longestPalindrome('cac'))
print(longestPalindrome('babad'))
print(longestPalindrome('abb'))
print(longestPalindrome('aaaa'))
print(longestPalindrome('aaa'))
print(longestPalindrome('aabafeeereser'))
