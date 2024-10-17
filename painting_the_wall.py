import math
def paint(height, width, coverage):
    area = height * width
    can_requirement =math.ceil( area / coverage )
    print(can_requirement)

paint(2,5,4)    