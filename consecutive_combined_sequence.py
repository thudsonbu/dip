# Write a function that returns True if two lists, when combined, 
# form a consecutive sequence.
from heapq import heappush, heappop, heapify

def consecutive_combined_sequence(arr1, arr2):
    # combone data sets
    data = arr1 + arr2
    heap = []
    # create a heap
    for item in data:
        heappush(heap, item)
    # poll heap for first element
    start = heap[0]
    end = heap[-1]
    sequence = True
    for i in range(start,end):
        if i == heappop(heap):
            continue
        else:
            sequence = False
    return sequence

print(consecutive_combined_sequence([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combined_sequence([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combined_sequence([1, 4, 5, 6], [2, 3, 7, 8, 10]))