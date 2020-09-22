# Hi, here's your problem today. This problem was recently asked by Google:

# Given two strings, find if there is a one-to-one mapping of characters between the two strings.

# Example
# Input: abc, def
# Output: True # a -> d, b -> e, c -> f

# Input: aab, def
# Ouput: False # a can't map to d and e 
# Here's some starter code:

def has_character_map(str1, str2):
    if len(str1) != len(str2): return False

    char_map = {}

    for i in range(len(str1)):
        if str1[i] not in char_map:
            char_map[str1[i]] = str2[i]
        else:
            if char_map[str1[i]] != str2[i]:
                return False
    
    return True

print(has_character_map('abc', 'def'))
 
print(has_character_map('aac', 'def'))
