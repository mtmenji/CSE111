"""
File: exercise2.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: Practice an code for an equation.
"""
#math needs to be imported to perform more complicated math.
#cmath needs to be imported to do the same thing but with complex numbers.
import cmath

def compute_data(a, b, c):
    return (-b + cmath.sqrt((b**2-4*a*c)))/(2*a)

print(compute_data(22, 66, 9))
print(compute_data(9, 1, 4))