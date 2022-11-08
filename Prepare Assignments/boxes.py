"""
File: boxes.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: Ask user for two inputs. 1) Number of items and 2) Number of items per box.
"""
import math

#Request the number of items and how many items per box from the user.
items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

#Calculate how many boxes are needed and round up for extra items!
box_total = math.ceil(items / items_per_box)

#Output the answer to the user.
print(f"For {items} items, packing {items_per_box} items in each box, you will need {box_total} boxes.")