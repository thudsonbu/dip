# Given a string, rearrange the string so that no character next to each other 
# are the same. If no such arrangement is possible, then return None.


def rearrangeString(string):
    letter_dict = create_letter_dict(string)
    priority_letters, other_letters = get_letters_to_poll(letter_dict)
    output_string = ""
    if len(priority_letters) == 1:
        letter_dict, output_string, possible = poll_single_highest(letter_dict, output_string)
    if possible:
        letter_dict, output_string = poll(letter_dict, output_string)
        return output_string
    else:
        return "Impossible"

def create_letter_dict(string):
    letter_dictionary = {}
    for letter_index in range(0,len(string)):
        letter = string[letter_index]
        try:
            letter_dictionary[letter] += 1
        except:
            letter_dictionary[letter] = 1
    return letter_dictionary

def get_letters_to_poll(letter_dict):
    sort_letters = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
    highest = sort_letters[0][1]
    if highest == 0:
        return [], []
    priority_letters = []
    other_pollable_letters = []
    for letter in sort_letters:
        if letter[1] == highest:
            priority_letters.append(letter[0])
        elif letter[1] > 0:
            other_pollable_letters.append(letter[0])
    return priority_letters, other_pollable_letters

def poll_single_highest(letter_dict, output_string):
    possible = True
    priority_letters, other_letters = get_letters_to_poll(letter_dict)
    other_letter_position = 0
    poll_highest = True
    while len(priority_letters) == 1:
        if poll_highest:
            letter_dict[priority_letters[0]] -= 1
            output_string += priority_letters[0]
            poll_highest = False
        else:
            if len(other_letters) > 1:
                if other_letter_position + 1 < len(other_letters) -1:
                    letter_dict[other_letters[other_letter_position]] -= 1
                    output_string += other_letters[other_letter_position]
                    other_letter_position += 1
                elif other_letter_position < len(other_letters) -1:
                    letter_dict[other_letters[other_letter_position]] -= 1
                    output_string += other_letters[other_letter_position]
                    other_letter_position = 0
            else:
                possible = False
            poll_highest = True
        priority_letters, other_letters = get_letters_to_poll(letter_dict)
    return letter_dict, output_string, possible

def poll(letter_dict, output_string):
    priority_letters, other_letters = get_letters_to_poll(letter_dict)
    while priority_letters:
        for letter in priority_letters:
            if letter != output_string[-1]:
                letter_dict[letter] -= 1
                output_string += letter
        priority_letters, other_letters = get_letters_to_poll(letter_dict)
    return letter_dict, output_string

print(create_letter_dict("aaabbbccccc"))
print(rearrangeString("acccbbaaabbbcbababbbcabaabbccccccccccccccccccccccccccccaa"))
    