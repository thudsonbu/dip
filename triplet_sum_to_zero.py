# Naive solution
# Pick a single number as a target, iterate though each number summing target and number
# find a third number (if any) that makes the sum zero
def triplet_finder(arr):
    combinations = []
    # set first num to test
    while len(arr) > 2:
        num = arr[0]
        arr.remove(num)
        combinations += combination_finder(arr,num)
    return combinations

def combination_finder(arr, num):
    combinations = [] # combinations that sum to zero
    used = [] # keeps track of second numbers that have already been used
    for i2 in range(0,len(arr)):
        num2 = arr[i2]
        for i3 in range(0,len(arr)):
            if i3 == i2 or i3 in used:
                continue
            else:
                num3 = arr[i3]
                if (num + num2 + num3) == 0:
                    used.append(i2)
                    print(used)
                    combinations.append([num,num2,num3])
    return combinations
        


input = [0,-1,2,-3,1]
input2 = [1,-2,1,0,5]

print(triplet_finder(input))
print(triplet_finder(input2))