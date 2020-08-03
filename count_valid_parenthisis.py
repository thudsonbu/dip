def count_invalid_parenthesis(string):
    open = 0
    closed = 0
    for letter in string:
        if letter == "(":
            open += 1
        elif letter == ")" and open > 0:
            open -= 1
        elif letter == ")":
            closed += 1 
    return closed + open

print(count_invalid_parenthesis("()())(())"))

