def excel_column_finder(num):
    num -= 1
    symbol = ["A"]
    count = 0
    while count < num:
        symbol = increment(symbol,-1)
        count += 1
    return "".join(symbol)


def increment(sym,loc):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if abs(loc) <= len(sym):
        if sym[loc] == "Z":
            sym[loc] = "A"
            return increment(sym,loc-1)
        else:
            letter_ind = letters.index(sym[loc])
            sym[loc] = letters[letter_ind + 1]
            return sym
    else:
        sym.insert(0,"A")
        return sym

print(excel_column_finder(5000))