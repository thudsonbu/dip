# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given a phone number, return all valid words that can be created using that phone number.

# For instance, given the phone number 364
# we can construct the words ['dog', 'fog'].


lettersMaps = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
    # either convert each word to numbers and check if sequence in number
    # go through number checking for word matches
        # need to keep track of where we are in a word
        # special category for word in progress
    found_words = []
    potential_words = []
    for number in phone:
        number_letters = lettersMaps[number]
        for i in range(0,len(potential_words)):
            potential_word = potential_words.pop(0)
            word, idx = potential_word[0], potential_word[1]
            
            if word[idx] in number_letters:
                if len(word) == idx + 1:
                    found_words.append(word)
                else:
                    potential_words.append((word,idx+1))
            
        for word in validWords:
            if word[0] in number_letters:
                if len(word) == 1:
                    found_words.append(word)
                else:
                    potential_words.append((word,1))
    
    return found_words

    

print(makeWords('364'))
# ['dog', 'fog']