# Hi, here's your problem today. This problem was recently asked by LinkedIn:

# Given two rectangles, find the area of intersection.

# Here's some starter code and a starter example:

class Rectangle():
  def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
    self.min_x = min_x
    self.min_y = min_y
    self.max_x = max_x
    self.max_y = max_y

def intersection_area(rect1, rect2):
    x_intersection = intersection_area_helper((rect1.min_x,rect1.max_x),(rect2.min_x,rect2.max_x))
    y_intersection = intersection_area_helper((rect1.min_y,rect1.max_y),(rect2.min_y,rect2.max_y))
    return x_intersection * y_intersection

def intersection_area_helper(values_1,values_2):
    overlap = 0
    for i in range(values_1[0],values_1[1]+1): 
        if i in range(values_2[0],values_2[1]+1):
            overlap += 1
    overlap = overlap-1 if overlap > 0 else overlap
    return overlap

#  BBB
# AXXB
# AAA
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)

print(intersection_area(rect1, rect2))
# 2