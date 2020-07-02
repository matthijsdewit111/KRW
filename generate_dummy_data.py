from random import random
from math import pi, sin, cos

amsterdam_center_long = 4.89
amsterdam_center_lat = 52.37
amsterdam_height = 0.1
amsterdam_width_ratio = 2


def get_random_point_in_amsterdam():
    angle = 2 * pi * random()
    lat_radius = (amsterdam_height / 2) * random()
    long_radius = lat_radius * amsterdam_width_ratio

    random_lat = lat_radius * sin(angle) + amsterdam_center_lat
    random_long = long_radius * cos(angle) + amsterdam_center_long

    return random_lat, random_long