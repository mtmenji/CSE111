import math
import random
from datetime import datetime

#Challenge 1 - Enter as many built-in functions in one line of code.
print(round(float(input("Enter a number with a decimal to round: "))))

#Challenge 2 - Execute the print function using 5 arguments.
print("Hello, I", 20, sep = " am ", end = " how old are you?", flush = True)

#Challenge 3 - Complete an equation and return a bool value indicating whether even (true) or odd (false).
def random_math():
    return ((math.ceil((17 ** 9) / 3)) - 6) % 2 == 0
print (random_math())

#Challenge 4 - Import the random package and make a list of random numbers. Sort from smallest to largest.
random_number_list = []
while len(random_number_list) < 10:
    random_number_list.append(random.randint(0, 1000))
random_number_list.sort()
print(random_number_list)

#Challenge 5 - If the computer clock has an even minute then print "even minute", same for odd minute.
now = datetime.now()
display_message = "even minute"
if (now.minute % 2 > 0):
    display_message = "odd minute"
print(display_message)