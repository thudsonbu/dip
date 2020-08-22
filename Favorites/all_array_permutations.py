# You are given an array of integers. Return all the permutations of this array.

def permute(nums):
    if len(nums) == 1:
        return nums
    out = [[nums[0],nums[1]],[nums[1],nums[0]]]
    if len(nums) == 2:
        return out
    for i in range(2,len(nums)):
        out = permute_helper(out, nums[i])
    return out
       
def permute_helper(current_perumutation_list, num_to_insert):
    new_permutation_list = []
    for permutation in current_perumutation_list:
        print(permutation)
        for i in range(0,len(permutation)+1):
            new_permutation_list.append(permutation[:i] + [num_to_insert] + permutation[i::])
    return new_permutation_list

print(permute([1,2,3]))