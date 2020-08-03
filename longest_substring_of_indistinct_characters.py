def find_longest(s, k):
    # record longest
    longest = []
    max_length = 0
    length = 0
    letter_count = 1
    # split string
    letters = [letter for letter in s]
    # add letters to longest and max length
    previous_letter = letters[0]
    for letter in letters:
        # append letter
        longest.append(letter)
        # length increases
        length += 1
        # if different add to letter count
        if letter != previous_letter:
            letter_count += 1
            # if letter count greater then three remove old letters
            if letter_count > 3:
                old_letter = longest.pop(0)
                length -= 1
                while old_letter == longest[0]:
                    longest.pop(0)
                    length = length -1
        # record length and check if change max
        length = len(longest)
        if length > max_length:
            max_length = length      
        previous_letter = letter

    return max_length

print(find_longest('aabc', 3))
print(find_longest('abcd', 3))
