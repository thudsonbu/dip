def check_overlap(tupple_a, tupple_b):
    start_a, end_a = tupple_a
    start_b, end_b = tupple_b
    return not (end_a < start_b or start_a > end_b)

def check_times(time_list):
    check_start = 0
    collision_array = []
    # Initialize collision count array
    for time in time_list:
        collision_array.append(0)

    # For each item iterate though check collisions with items
    # As each item is checked it is eliminated from the check list as not to double count
    while check_start < len(time_list):
        for i in range(check_start + 1, len(time_list)):
            collision_found = check_overlap(time_list[check_start], time_list[i])
            if collision_found:
                collision_array[check_start] += 1
                collision_array[i] += 1
        check_start += 1

    return max(collision_array)

print(check_times([(30, 75), (0, 50), (60, 150)]))
        
