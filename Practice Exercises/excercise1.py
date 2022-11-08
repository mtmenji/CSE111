"""
File: exercise1.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: Practice an code for an equation.
"""

def compute_data(a, b, c, d):
    return (a/b)*(a/((c**2+d**2)))

def test_data():
    #Declare test data.
    data = []
    data.append([5, 4, 3, 2, 0.4807692307692308])
    data.append([9, 1, 4, 6, 1.5576923076923077])
    
    #Loop run tests.
    for test in data:
        print(compute_data(test[0], test[1], test[2], test[3]) == test [4])

test_data()