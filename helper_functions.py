import math


# Calculate the length of a 2D vector
def length(vel):
    return math.sqrt(vel[0] ** 2 + vel[1] ** 2)


# Normalize a 2D vector
def normalize(vel):
    if length(vel) != 0:
        return [vel[0]/length(vel), vel[1]/length(vel)]
    else:
        return 0, 0
