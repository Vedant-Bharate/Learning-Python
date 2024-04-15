# Activity Python: CFU Task 2
# File: HW_11p2_Task1_bharatva
# Date: 16 11 2023
# By: Vedant B
# Section: 021
# Team: 359

# ELECTRONIC SIGNATURE
# Vedant Bharate

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This program determines

# Importing Required Libraries
import random
import math

# Getting required inputs
n = int(input("Specify number of times to flip the coin: "))

# Initialising Variables
heads = 0
tails = 0

# Setting up the Counter Loop
for number in range(n):
    flip = random.randint(0, 1)
    print(flip)
    if flip == 0:
        tails = tails + 1
    else:
        heads = heads + 1

# Printing the number of heads or tails
print("Number of Heads: {0}, Number of Tails: {1}".format(heads, tails))

# Determining the Percentage
PH = (heads / n) * 100
PT = (tails / n) * 100
print("Percentage of Flips that were Heads: {0:.2f}, Percentage of Flips that were Tails: {1:.2f}".format(PH, PT))
