# Given a string of digits, return the longest substring with alternating odd/even or 
# even/odd digits. If two or more substrings have the same length, return the substring 
# that occurs first. Perform the operations in constant space and time.

def longest_alt_substring(digits):
    long_start = long_end = long_length = current_start = current_end = current_length = 0
    for index in range(1,len(digits)):
        current_digit = int(digits[index])
        previous_digit = int(digits[index-1])
        if different(previous_digit, current_digit):
            current_end = index
            current_length += 1
            if current_length > long_length:
                long_start = current_start
                long_end = current_end
                long_length = current_length
        else:
            current_start = index
            current_length = 0
        
    return digits[long_start:long_end+1]

def different(num,num2):
    out = True
    if (num % 2) == (num2 % 2):
        out = False
    return out

print(longest_alt_substring("225424272163254474441338664823"))
print(different(1,2))