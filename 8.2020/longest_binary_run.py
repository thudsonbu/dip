def create_binary(num):
    binary = ["0"]
    count = 0
    while count < num:
        binary = increment(binary,-1)
        count += 1
    return binary

def increment(binary,pos):
    if abs(pos) <= len(binary):
        if binary[pos] == "0":
            binary[pos] = "1"
            return binary
        elif binary[pos] == "1":
            binary[pos] = "0"
            return increment(binary, pos-1)
    else:
        binary.insert(0,"1")
        return binary

def find_longest_run(binary):
    longest, current = 0, 0
    for i in range(0,len(binary)):
        if binary[i] == "1":
            current += 1
            longest = max(current,longest)
        else:
            current = 0
    return longest
        
binary = create_binary(4)
print(binary)
print(find_longest_run(binary))