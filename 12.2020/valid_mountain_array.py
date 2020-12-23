# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given an array of heights, determine whether the array forms a "mountain" pattern. A mountain pattern goes up and then down.

# Like
#   /\
#  /  \
# /    \


class Solution(object):

    def valid_mountain_array(self, arr):
        
        if len(arr) <= 1:
            return False

        pos = 1
        while arr[pos - 1] <= arr[pos]: # while moving upward
            if pos < (len(arr) - 1): # if we havent reached end continue
                pos += 1
            else: # if we have reached the end not mountain (should go down)
                return False
        
        while arr[pos - 1] >= arr[pos]: # while moving down
            if pos == (len(arr) - 1): # if we reach end its a mountain
                return True
            pos += 1

        return False # did not reach end going down, not a mountain

    def valid_mountain_array_state(self, arr):
        rising = True

        for i in range(1,len(arr)):
            left = arr[i-1]
            right = arr[i]

            if left <= right and rising: 
                continue
            elif rising:
                rising = False
            elif left >= right and not rising:
                continue
            else:
                return False
        
        return not rising


    

print(Solution().valid_mountain_array([1, 2, 3, 2, 1]))

print(Solution().valid_mountain_array([1, 2, 3]))


print(Solution().valid_mountain_array_state([1, 2, 3, 2, 1]))

print(Solution().valid_mountain_array_state([1, 2, 3]))
