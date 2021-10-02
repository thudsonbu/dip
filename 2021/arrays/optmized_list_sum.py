# Create a class that initializes with a list of numbers and has one method
# called sum. sum should take in two parameters, start_idx and end_idx and
# return the sum of the list from start_idx (inclusive) to end_idx` (exclusive).

class ListFastSum:
  def __init__(self, nums):
    self.nums = nums
    self.sums = []

    total = 0
    for num in nums:
      self.sums.append( total )
      total += num

  def sum(self, start_idx, end_idx):
    return self.sums[end_idx] - self.sums[start_idx]

print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
