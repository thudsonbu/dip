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

#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]