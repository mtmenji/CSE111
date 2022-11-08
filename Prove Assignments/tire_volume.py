"""
File: tire_volume.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: Request tire info from user. Output the volume of their tire. Also, output information to a text file.
Extra: Created an if statement asking if user would like to purchase tires. If yes, the program will ask user for phone number and append that info the created text file as well.
"""

import math
import datetime

#Receive input variables from user and convert to int for math.
width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#Calculate output variable.
volume = round(((math.pi*(width**2)*ratio*(width*ratio+2540*diameter))/10000000000), 2)

#Output answer to user.
print(f"The approximate volume is {volume:.2f} liters.")

current_date = datetime.date.today()

#I could not figure out how to apend to a file with a comma separator, so I just converted all the variables to strings and concatenated them together with the commas. I'm hoping to figure out a better way to do this.
current_date_str = str(current_date)
width_str = str(width)
ratio_str = str(ratio)
diameter_str = str(diameter)
volume_str = str(volume)
file_output = current_date_str + ", " + width_str + ", " + ratio_str + ", " + diameter_str + ", " + volume_str

with open("volumes.txt", "at") as volumes_file:
    print(file_output, file = volumes_file)

#Extra code to the assignment. Appends phone number to text file if user answers yes.
buy_tires = input("Are you looking to buy tires with the dimensions provided? (y/n)")
if buy_tires == "y":
    phone = input("Great! What is your phone number, so we can contact you?")
    with open("volumes.txt", "at") as volumes_file:
        print(phone, file = volumes_file)
