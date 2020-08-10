# Given an element in a list, write a function to determine 
# the length of a particular element's sorting cycle. Given 
# one element in the list, a sorting cycle is the number of 
# swaps it takes so that the last displaced swapped item is 
# back in its correct order.

def cycle_length(lst, n):
    count = 0
    sorted_list = sorted(lst)
    while True:
        current_position = lst.index(n)
        ideal_position = sorted_list.index(n)
        if current_position != ideal_position:
            lst[current_position] = lst[ideal_position]
            lst[ideal_position] = n
            n = lst[current_position]
            count += 1
        else:
            break
    return count

print(cycle_length([1, 9, 8, 4, 7, 2, 6, 3, 5],9))

            