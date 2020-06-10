# Project 2
# Irvan Tristian - 0447356121-105

import random

priority = 1
email = 'irvantristian@gmail.com'

# Check whether a coordinate is in circle or not
def isPointInCircle(x, y, r, center=(0, 0)):
    return (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r ** 2

# Generate a list of random coordinates in a square form
def generateRandomSquarePoints(n, length, center=(0, 0)):
    minx = center[0] - length / 2
    miny = center[1] - length / 2
    points = [[random.uniform(minx, center[0] + length / 2), random.uniform(miny, center[1] + length / 2)]
              for point in range(n)]
    return points

# Calculate an estimated circle area
def MCCircleArea(r, n=100, center=(0, 0)):
    points_list = generateRandomSquarePoints(n, 2 * r, center)
    in_circle = sum(isPointInCircle(i[0], i[1], r, center) for i in points_list)
    square_area = (2 * r) ** 2
    return (in_circle / n) * square_area

# Calculate an estimated pi value 
def LLNPiMC(nsim, nsample):
    return sum(MCCircleArea(1, nsample) for i in range(nsim)) / nsim

# Calculate relative error percentage of an estimated pi
def relativeError(act, est):
    return abs((est - act) / act * 100)

if __name__ == "__main__":
    # Function 1 check
    print(isPointInCircle(1, 1, 1, center=(0, 0)), isPointInCircle(1, 0, 1, center=(0, 0)),
          isPointInCircle(1, 1, 1, center=(1, 0)), isPointInCircle(0, 0, 1, center=(1, 1)))
    
    # Function 2 check
    random.seed(0)
    points = generateRandomSquarePoints(100, 1)
    print(points[10:15])

    # Function 3 check
    random.seed(0)
    print(MCCircleArea(1, 100), MCCircleArea(1, 10, center=(10, 10)))
    
    # Function 4 check
    import math
    random.seed(0)
    estpi = LLNPiMC(10000, 500)
    print('est_pi:', estpi)
    print('act_pi:', math.pi)

    # Function 5 check
    print('error relatif:', relativeError(math.pi, estpi), '%')
