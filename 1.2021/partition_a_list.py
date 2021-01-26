# Given a list of numbers and an integer k, partition/sort the list such
# that all numbers less then k occur before k, and all numbers greater
# than k occur after the number k

def partition_list( nums, k ):
  smaller = 0
  equal = 0
  larger = len( nums ) - 1

  while equal <= larger:
    num = nums[equal]

    if num < k:
      nums[smaller], nums[equal] = nums[equal], nums[smaller]
      smaller += 1
      equal += 1

    if num == k:
      equal += 1
      
    if num > k:
      nums[larger], nums[equal] = nums[equal], nums[larger]
      larger -= 1

  return nums

out = partition_list( [ 2, 2, 2, 5, 2, 2, 2, 2, 5 ], 3 )
print( out )
print('should be \n[2, 2, 2, 2, 2, 2, 2, 2, 5]')