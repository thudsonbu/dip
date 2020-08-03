def reverse_words(string):
    words = string.split()
    out = ""
    for word in words:
        if word == words[-1]:
            word = word[0:-1]
            new_word = word[::-1]
            out += new_word + "."
        else:
            new_word = word[::-1]
            out += new_word + " "
    return out

print(reverse_words("The thing is good."))