"""
File: provinces.py
Author: Michael Menjivar
Course: CSE 111-04

Purpose: Create a compound list variable from information read from a text file (provinces.txt).
"""
compound_list = []

with open('provinces.txt', 'rt') as text_file:
    for line in text_file:
        clean_line = line.strip()
        compound_list.append(clean_line)
print(compound_list)

compound_list.pop(0)
print(compound_list)

compound_list.pop(-1)
print(compound_list)

for i in range(len(compound_list)):
    if compound_list[i] == 'AB':
        compound_list[i] = 'Alberta'

count = compound_list.count('Alberta')

print(count)