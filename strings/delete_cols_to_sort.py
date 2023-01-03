# You are given an array of n strings strs, all of the same length. The strings
# can be arranged such that there is one on each line, making a grid. For
# example, strs = ["abc", "bce", "cae"] can be arranged as:

# abc
# bce
# cae

# You want to delete the columns that are not sorted lexicographically. In the
# above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are
# sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

# Return the number of columns that you will delete.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # If there are no strings there is nothing to delete
        if not strs:
            return 0

        del_ct = 0

        # For each character index
        for i in range(0, len(strs[0])):
            # Record the previous word's character
            prev_char = strs[0][i]

            # Go through each word selecting the character at that index
            for j in range(1, len(strs)):
                cur_char = strs[j][i]

                # If the new character has a higher ascii value (indicating that it has a higher lexicographical value)
                if ord(cur_char) < ord(prev_char):
                    # This col should be deleted so increment count and move to next col
                    del_ct += 1
                    break
                 # Otherwise
                else:
                    # Continue to next character in the column
                    prev_char = cur_char

        return del_ct
