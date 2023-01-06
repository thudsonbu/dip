class Solution:
    def rob(self, nums):
        store = [-1 for n in nums]

        return self.robRecursive(-2, nums, store)

    def robRecursive(self, i, nums, store):
        house1, house2 = 0, 0

        if i + 2 <= len(nums) - 1:
            if store[i+2] != -1:
                house1 = store[i+2]
            else:
                house1 = self.robRecursive(i + 2, nums, store)

        if i + 3 <= len(nums) - 1:
            if store[i+3] != -1:
                house2 = store[i+3]
            else:
                house2 = self.robRecursive(i + 3, nums, store)

        max_path = max(house1, house2)

        if i >= 0:
            store[i] = max_path + nums[i]
            return max_path + nums[i]
        else:
            return max_path
