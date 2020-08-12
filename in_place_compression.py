# Given an array of characters with repeats, compress it in place. The length 
# after compression should be less than or equal to the original array.

def compress_in_place(chars):
    location = 0
    current_char = chars[location]
    current_char_count = 1
    accounted_for = 0
    while accounted_for < len(chars):
        if location + current_char_count < len(chars) and current_char == chars[location + current_char_count]:
            current_char_count += 1
            accounted_for += 1
        elif current_char_count > 1:
            chars[location + 1] = current_char_count
            location += 2
            for i in range(2,current_char_count):
                chars.pop(location)
            if location < len(chars):
                current_char = chars[location]
            else:
                break
            current_char_count = 1
        else:
            location += 1
            accounted_for += 1
            current_char_count = 1
            if location < len(chars):
                current_char = chars[location]
            else:
                break
    return chars

def compress_in_place2(chars):
    left = i = 0
    while i < len(chars):
        char, length = chars[i], 1
        while (i + 1) < len(chars) and char == chars[i + 1]:
            length, i = length + 1, i + 1
        chars[left] = char
        if length > 1:
            len_str = str(length)
            chars[left + 1:left + 1 + len(len_str)] = len_str
            left += len(len_str)
        left, i = left + 1, i + 1 
    return chars[:left]

def compress_in_place3(chars):
    left = 1
    while left < len(chars):
        if chars[left -1] == chars[left]:
            count = 2
            next_letter = left + 1
            while next_letter < len(chars):
                if chars[next_letter] == chars[left]:
                    count += 1
                    del chars[next_letter]
                else:
                    break
            chars[left] = count
        left += 1
    return chars


print(compress_in_place(['a','a','b','c','c','c','c','a','a','a']))
print(compress_in_place2(['a','a','b','c','c','c','c','a','a','a']))
print(compress_in_place3(['a','a','b','c','c','c','c','a','a','a']))
