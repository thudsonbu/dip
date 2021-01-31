# Given a list of positive integers find the largest possible set such that no
# elements are adjacent numbers of each other.

def max_non_adjacent_sum( nums ):

  current_max_sum = 0
  previous_max_sum = 0

  for num in nums:
    t = current_max_sum
    current_max_sum = max( current_max_sum, previous_max_sum + num )
    previous_max_sum = t

  return current_max_sum

assert max_non_adjacent_sum( [3, 4, 1, 1] ) == 5
assert max_non_adjacent_sum( [2, 1, 2, 7, 3] ) == 9