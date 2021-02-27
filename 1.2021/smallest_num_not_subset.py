# Given a sorted list of positive numbers, find the smalleds positve number
# that cannot be a sum of any subset in the list.

def find_smallest( nums ):

  res = 1

  for n in nums:
    if n <= res:
      res += n
    else:
      break

  return res

assert find_smallest( [ 1, 2, 3, 8, 9, 10 ] ) == 7