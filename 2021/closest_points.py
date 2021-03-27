# Given a list of points, an interger k, and a point p, find the k closest points to p.

import math

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return "[" + str(self.x) + "," + str(self.y) + "]"


def closest_points(points, k, p):
  closest_points = []

  for point in points:
    dist = find_distance(p, point)

    if len(closest_points) < 1:
      closest_points.append([dist, point])

    elif len(closest_points) < k:
      closest_points = insert_point(closest_points, dist, point)

    elif dist < closest_points[0][0]:

      del closest_points[0]

      closest_points = insert_point(closest_points, dist, point)

  return [ p[1] for p in closest_points ]


def insert_point(closest_points, dist, point):
  pos = 0

  while dist < closest_points[pos][0]:
    pos += 1

    if pos >= len(closest_points) - 1:
      break

  closest_points.insert(pos, [dist, point])

  return closest_points


def find_distance(p1, p2):
  x_dif = p1.x - p2.x
  y_dif = p1.y - p2.y
  return ( x_dif**2 + y_dif**2 )**.5

points = [
  Point(0, 0),
  Point(1, 1),
  Point(2, 2),
  Point(3, 3),
]
print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]
