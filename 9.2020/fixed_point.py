# Hi, here's your problem today. This problem was recently asked by Apple:

# A fixed point in a list is where the value is equal to its index. So for example the list
# [-5, 1, 3, 4], 1 is a fixed point in the list since the index and value is the same. Find 
# a fixed point (there can be many, just return 1) in a sorted list of distinct elements, 
# or return None if it doesn't exist.


# BINARY SEARCH SOLUTION
def find_fixed_point2(start_index, nums): # start index should be 0 when first called
    print("Numbers: " + str(nums) + " Start index: " + str(start_index))
    mid = int(len(nums)/2)
    if len(nums) == 0:
        return None
    elif nums[mid+start_index] == mid+start_index:
        return nums[mid+start_index]
    elif nums[mid+start_index] > mid+start_index:
        return find_fixed_point2(start_index,nums[0:mid])
    else:
        return find_fixed_point2(mid,nums[mid+1::])
        

print(find_fixed_point2(0,[-5,1,4,5,6,10]))
print(find_fixed_point2(0,[-5,2,3,6,9]))
print(find_fixed_point2(0,[-5,1,3,6,9]))
print(find_fixed_point2(0,[-1]))


# BAD SOLUTION
def find_fixed_point(nums):
    if nums[0] > 0 or nums[len(nums) - 1] < len(nums)-1:
        return None
    upper_dif = nums[len(nums)-1] - len(nums)-1
    lower_dif = 0 - nums[0]

    if lower_dif < upper_dif:
        print("Lower is closer")
        i = 0
        while i < len(nums):

            if i+5 > len(nums):
                step_index = i
                while step_index < len(nums):
                    if nums[step_index] == step_index:
                        return nums[step_index]
                    step_index += 1
                return None

            elif nums[i] == i:
                return i

            elif nums[i] > i:
                reverse_index = -1
                while reverse_index > -4:
                    if nums[i-reverse_index] == i-reverse_index:
                        return nums[i-reverse_index]
                    reverse_index -= 1
                return None

            i += 5

        return None
    
    else:
        print("Higher is closer")
        i = len(nums)-1
        while i >= 0:

            if i-5 <= 0:
                step_index = i
                while step_index >= 0:
                    if nums[step_index] == step_index:
                        return nums[step_index]
                    step_index -= 1
                return None

            elif nums[i] == i:
                return i
            
            elif nums[i] < i:
                reverse_index = +1
                while reverse_index < 4:
                    if nums[i+reverse_index] == i+reverse_index:
                        return i+reverse_index
                    reverse_index += 1
                return None

            i -= 5
        
        return None

print(find_fixed_point([-5,1,3,4]))


            

