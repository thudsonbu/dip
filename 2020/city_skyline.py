# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given a list of building in the form of (left, right, height), return what the skyline should look like.
# The skyline should be in the form of a list of (x-axis, height), where x-axis is the next point where 
# there is a change in height starting from 0, and height is the new height starting from the x-axis.

# Here's some starter code:

def generate_skyline(buildings):
    skyline = []
    for building in buildings:
        while len(skyline) <= building[1] + 1:
            skyline.append(0)
        for i in range(building[0],building[1]+1):
            if skyline[i] < building[2]:
                skyline[i] = building[2]
    current_height = 0
    out = []
    for i in range(0,len(skyline)):
        if skyline[i] != current_height:
            out.append((i,skyline[i]))
            current_height = skyline[i]
    return out

import heapq


def generate_skyline(buildings):
    tallest = []
    skyline = []

    buildings += [(x + 1, x + 1, 0) for (_, x, _) in buildings]
    buildings.sort(key=lambda x: (x[0], -x[2]))

    for l, r, h in buildings:
    # Remove shorter buildings behind current building.
        while tallest and l >= tallest[0][1]:
            heapq.heappop(tallest)

        # Add current building to heap.
        heapq.heappush(tallest, (-h, r))

        # Append to skyline if the building is not the tallest.
        if not skyline or skyline[-1][1] != -tallest[0][0]:
            skyline.append((l, -tallest[0][0]))

    return skyline


#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]