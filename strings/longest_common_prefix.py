# Write a function to find the longest common prefix string amongst an array of
# strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs):
        longest_prefix = strs[0]

        for i in range(1, len(strs)):
            cur_string = strs[i]

            # Maximum possible length of prefix cannot be greater than length of
            # current string
            max_len = min(len(longest_prefix), len(cur_string))

            while cur_string[0:max_len] != longest_prefix[0:max_len]:
                max_len -= 1

                if max_len == 0:
                    return ''

            longest_prefix = longest_prefix[0:max_len]

        return longest_prefix

sol = Solution()

assert sol.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
assert sol.longestCommonPrefix(['dog', 'racecar', 'car']) == ''
assert sol.longestCommonPrefix(['']) == ''
assert sol.longestCommonPrefix(['a']) == 'a'
assert sol.longestCommonPrefix(['a', 'b']) == ''
assert sol.longestCommonPrefix(['a', 'a']) == 'a'
assert sol.longestCommonPrefix(['ab', 'a', 'ab']) == 'a'
