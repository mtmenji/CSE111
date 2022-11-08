"""
File: exercise2.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: Practice an code for an equation.
"""

import math

def compute_area(r):
    return math.pi * r**2

radius = float(input("Please input a radius: "))

print(f"The area is: {compute_area(radius)}")