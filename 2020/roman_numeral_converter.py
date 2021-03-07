# Given a Roman numeral, find the corresponding decimal value. Inputs will 
# be between 1 and 3999.

def roman_numeral_converter(input):
    # make value dictionary
    val_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    numerals = ["M","D","C","L","X","V","I"]
    nums = [num for num in input]

    running_sum = 0

    # iterate though adding each number to running sum
    while len(nums) > 1:
        num1 = nums[0]
        num2 = nums[1]
        # if num 1 is less then num 2
        if val_dict[num1] < val_dict[num2]:
            # add val 2 less val one and remove them both
            running_sum += val_dict[num2] - val_dict[num1]
            nums.pop(0)
            nums.pop(0)
        # otherwise add the number and remove it
        else:
            running_sum += val_dict[num1]
            nums.pop(0)

    # add last digit
    if len(nums) > 0:
        running_sum += val_dict[nums[0]]

    return running_sum

print(roman_numeral_converter("MCMIV"))