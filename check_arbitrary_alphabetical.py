# create order dictionary

# map values in word to dictionary while checking order

def check_alphabet(words, dictionary):
    order_mapping = {char: idx for idx, char in enumerate(dictionary)}
    order = True
    for word in words:
        letters = [letter for letter in word]
        numbers = []
        for letter in letters:
            numbers.append(order_mapping[letter])
        print(numbers)
        if sorted(numbers) != numbers:
            order = False
    return order
    
print(check_alphabet(["zyx", "zyxw", "zyxwv"],"zyxwvutsrqponmlkjihgfedcba"))
print(check_alphabet(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))