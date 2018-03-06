"""Calculating pi using the Monte Carlo Method"""

import random

def pi(n, r):
    """Return coordinates after n block random walk"""
    inside_circle = 0
    inside_square = 0
    for i in range(n):
        (x, y) = random.random()*r, random.random()*r
        inside_square += 1
        if x**2 + y**2 <= r**2:
            inside_circle += 1
    pi_approx = (4 * inside_circle) / inside_square
    return pi_approx

print(pi(10000, 1))
