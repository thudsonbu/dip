# given two strings, determine the edit distance between them. The edit distance
# is defined as the minumum number of edits (insertion, deletion, substitution)
# needed to change on string to the other

# this problem is best solved recursively. First, if a string is empty, we will
# need to insert all letters, so the edit distance is the difference between
# the two.

def distance(s1, s2):
    # if there are not letter in one the distance is all letters in the other
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))

    # remove first letter of first string ( add 1 as we skipped a letter )
    first = distance(s1[1:], s2) + 1

    # remove first letter of second string ( add 1 as we skipped a letter )
    second = distance(s2[1:], s1) + 1

    # if they are the same letter then we dont add any
    if s1[0] == s2[0]:
        same = distance(s1[1:], s2[1:])
    # if they are different we skip the letter ( add 1 )
    else:
        same = distance(s1[1:], s2[1:]) + 1

    return min(first, second, same)


edit_distance = distance('potato', 'tomato')

print(edit_distance)
