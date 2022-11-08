"""
File: heart_rate.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: 
"""

"""
Outline for code:
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
# Ask user for their age while simultaneously converting the
# input to an int. 
age = int(input("Please enter your age: "))

# Calculations. Determing the maximum heart rate and the min/max
# range for the user's heart rate. Converted variables to ints
# for rounding purposes.
maxHeartRate = int(220 - age)
minRange = int(maxHeartRate * .65)
maxRange = int(maxHeartRate *.85)

# Output to the user their heart rate range using an f-string
# to display a message with the numbers from the ints.
print("When you exercise to strengthen your heart, you should "
    f"keep your heart rate between {minRange} and {maxRange} "
    "beats per minute.")
