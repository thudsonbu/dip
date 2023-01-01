# Given a `pattern` and a string `s`, find if `s` follows the same pattern.

# Here *follow* means a full match, such that there is a bijection between a
# letter in the pattern and a non-empty word in s.

# Each letter should match to a word in the input string. For example
# - Input: `pattern` = `"abba"` and `s` = `dog cat cat dog`
# - Output: `true`

# Because `a => dog` and `b => cat`.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = dict()
        words_used = set()

        for i in range(0, len(words)):
            char = pattern[i]
            word = words[i]

            if char in char_to_word and char_to_word[char] != word:
                return False
            elif char not in char_to_word and word in words_used:
                return False
            else:
                char_to_word[char] = word
                words_used.add(word)

        return True
