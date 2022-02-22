# arr you go from os
arr = [ 'file100.txt', 'file1.txt', 'file4.txt' ]

def get_file_key( filename ):
  characters = list( filename )

  firstNumIndex = 0
  lastNumIndex  = len(characters) - 4

  for i in range( 0, len(characters) ):

    # cheeky way to check if its between 1 - 9 using ascii encoding
    if ord( characters[i] ) < 58 and ord( characters[i] ) > 47:
      firstNumIndex = i
      break

  prefix = '0' * ( 3 - ( lastNumIndex - firstNumIndex ) )

  key = prefix + filename[ firstNumIndex:lastNumIndex ]

  return key

arr.sort( key=get_file_key )

print( arr )
