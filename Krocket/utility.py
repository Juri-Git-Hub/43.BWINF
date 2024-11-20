from shapely.geometry import LineString
from math import degrees, atan2


def linear_function(point1, point2):
    # this function returns m and b for a linear function f(x) = mx + b
    x1, y1 = point1
    x2, y2 = point2

    # Handle vertical line case
    if x1 == x2:
        return None, None  # Indicates a vertical line

    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    return m, b


def check_intersection(p1, p2, q1, q2):
    # this function checks whether two lines intersects
    line1 = LineString([p1, p2])
    line2 = LineString([q1, q2])

    intersection = line1.intersection(line2)

    if intersection.is_empty:
        return False, (-1, -1)
    else:
        if isinstance(intersection, LineString):
            return True, (-1, -1)
        else:
            return True, (intersection.x, intersection.y)


def calculate_angle(a, x, b):
    # this function calculates the angle for three given points
    x1, y1 = a
    x2, y2 = x
    x3, y3 = b
    deg1 = (360 + degrees(atan2(x1 - x2, y1 - y2))) % 360
    deg2 = (360 + degrees(atan2(x3 - x2, y3 - y2))) % 360

    angle = deg2 - deg1 if deg1 <= deg2 else 360 - (deg1 - deg2)
    return angle
