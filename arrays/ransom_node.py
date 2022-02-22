# A criminal is constructing a ransom note. In order to disguise his handwriting, 
# he is cutting out letters from a magazine.

# Given a magazine of letters and the note he wants to write, determine whether 
# he can construct the word.

def canSpell( magazine, note ):
  note_letters = [ letter for letter in note ]
  note_dict = { letter : True for letter in note_letters }

  for letter in magazine:
    if note_dict.get(letter):
      note_dict.pop(letter)
  
  return len(note_dict) == 0
  
print(canSpell([ 'a', 'b', 'c', 'd', 'e', 'f' ], 'bed'))
print(canSpell([ 'a', 'b', 'c', 'e', 'f' ], 'bed'))
