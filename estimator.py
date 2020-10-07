from random import random as rdn

def estimate_pi(num_points:int):
    points = []
    for i in range(num_points):
        points.append((rdn(),rdn()))
    print(points)

estimate_pi(2)       