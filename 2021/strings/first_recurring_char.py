# Given a string, return the first recurring letter that appears. If there is 
# no recuring letters, return none

def first_recurring_char(s):

  index = 1
  while(index < len(s)):
    if s[index] == s[index-1]:
      return s[index]

    index += 1
  
  return None

print(first_recurring_char('qwertty'))

print(first_recurring_char('qwerty'))
