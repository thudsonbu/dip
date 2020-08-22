# Given a non-empty array where each element represents a digit of a non-negative integer,
# add one to the integer. The most significant digit is at the front of the array and each 
# element in the array contains only one digit. Furthermore, the integer does not have leading 
# zeros, except in the case of the number '0'.

def plusOne(arr):
    for index in reversed(range(0,len(arr))):
        if arr[index] == 9:
            arr[index] = 0
        else:
            arr[index] += 1
            break
    return arr

def plusOne2(arr):
    num = 0
    for i in range(len(arr)):
      num = num*10 + arr[i]
    return [int(i) for i in str(num+1)]

print(plusOne([3,9,9]))
print(plusOne2([2,4,9]))