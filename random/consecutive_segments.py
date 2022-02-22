def findRanges(nums):
    out = []
    start = nums[0]
    end = nums[0]
    for i in range (0, len(nums)):
        # If last item append current state
        if i == len(nums)-1:
            out.append(str(start) + "->" + str(nums[i]))
        # If the next item is not consecutive append current state
        elif nums[i] + 1 < nums[i+1]:
            out.append(str(start) + "->" + str(nums[i]))
            # Reset to next item
            start = nums[i+1]
            end = nums[i+1]
        # Otherwise set a new end to the segment
        else:
            end = nums[i]
    return out
      

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']