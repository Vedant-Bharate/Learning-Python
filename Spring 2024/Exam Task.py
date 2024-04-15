# File: ACT_Python_6p2_Team319_bharatva.py
# Date: 25 January 2024
# By: Vedant Bharate
# Section: 018
# Team: 319
#
# ELECTRONIC SIGNATURE
# Vedant Bharate
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This program reads a list of snowfall data and then returns the date on which highest snowfall was recorded.

# Opening the file to read
snows = open('Snow_Fall.txt', 'r')
Lines = snows.readlines()
snows.close()
maxsnow = []
f = 0
g = 1
d = 0

for i in range(0,len(Lines)):
    Lines[i] = Lines[i].split()

# Reading when the snow is highest
for j in range(0,len(Lines)):
    maxsnow.append(float(Lines[f][g]))
    f += 1

snow_index = maxsnow.index(max(maxsnow))

# Reading the number of days snow is higher than 1
for k in range(0,len(maxsnow)):
    if maxsnow[k] > 1:
        d += 1

# Calculating percent
percent = d/len(maxsnow) * 100
# Printing the output
print("Maximum snowfall: {0:.2f} inches on ".format(float(max(maxsnow))) + Lines[snow_index][0])
print("Percentage of days snowfall exceeded 1 inch: {0:.3f} ".format(percent) + "%")
