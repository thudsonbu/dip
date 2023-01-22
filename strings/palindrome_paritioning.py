class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPalindrome(s):
            n = len(s)

            if n == 1:
                return True

            center = n//2

            left = s[0:center]
            right = s[center+(n%2)::]

            return left == right[::-1]

        def helper(i, s, n, memo):
            if i >= len(s):
                return [[]]

            if memo[i] != None:
                return memo[i]

            palindromes = []

            for j in range(i+1,n+1):
                if checkPalindrome(s[i:j]):
                    sub_palindromes = helper(j, s, n, memo)

                    for combination in sub_palindromes:
                        palindromes.append([s[i:j], *combination])

            memo[i] = palindromes

            return palindromes

        n = len(s)

        memo = [None for _ in s]
        memo[n-1] = [[s[n-1]]]

        return helper(0, s, n, memo)
