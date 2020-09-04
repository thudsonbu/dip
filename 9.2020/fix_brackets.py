# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a string with only ( and ), find the minimum number of characters to add or subtract to fix the string such that the brackets are balanced.

# Example:
# Input: '(()()'
# Output: 1
# Explanation:

# The fixed string could either be ()() by deleting the first bracket, or (()()) by adding a bracket. These are not the only ways of fixing the string, there are many other ways by adding it in different positions!


# Here's some code to start with:

def fix_brackets(s):
    currently_open_brackets = 0
    needed_brackets = 0
    for i in range(len(s)):
        bracket = s[i]
        if bracket == '(':
            currently_open_brackets += 1
        elif bracket == ')':
            if currently_open_brackets > 0:
                currently_open_brackets -= 1
            else:
                needed_brackets += 1
    needed_brackets += currently_open_brackets
    return needed_brackets

print("0 is " + str(fix_brackets('')))
print("0 is " + str(fix_brackets('(()())')))
print("1 is " + str(fix_brackets(')')))
print("1 is " + str(fix_brackets('(')))
print("2 is " + str(fix_brackets("kalsdfkjfe()))")))
print("2 is " + str(fix_brackets('((')))
print("3 is " + str(fix_brackets('((()()))))(')))
