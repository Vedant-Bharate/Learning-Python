# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team359_bharatva.py
# Date: 26 10 2005
# By: Vedant B
# Section: 021
# Team: 359

# ELECTRONIC SIGNATURE
# Vedant Bharate

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This program calculates the V2 i.e. the speed of the roller-coaster at point 2.
# Importing required Libraries
import math

# Initialising Variable and getting the input
v1 = float(input("Enter the car speed at position 1 (v1): "))
f = float(input("Enter the friction coefficient (f): "))
d = float(input("Enter the traveled distance (d): "))
y1 = float(input("Enter the initial elevation (y1): "))
y2 = float(input("Enter the final elevation (y2): "))

# Defining Formula
P1 = (v1**2) - ((f * d) * 9.81)
P2 = (9.81 * (y1 - y2)) * 2
v2 = math.sqrt(P1 + P2)

# Giving the output
print('The total value of V2 = {0:.2f} m/s'.format(v2))
