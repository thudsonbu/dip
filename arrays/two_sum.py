# You are given a list of numbers, and a garget number k. Return wheter or not 
# there are two numbers in the list that add up to k

def two_sum(nums, target):
  
  sum_arr = []

  for num in nums:
    if num in sum_arr:
      return True

    else:
      miss = num - target

      if miss < 0:
        sum_arr.append( -miss )
      elif miss > 0:
        sum_arr.append( miss )
      else:
        sum_arr.append( 0 )

  return False

print(two_sum([4,7,1,-3,2], 5))