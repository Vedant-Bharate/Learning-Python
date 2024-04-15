# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team359_bharatva.py
# Date: 26 10 2005
# By: Vedant B
# Section: 021
# Team: 359
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
# This script is a header template that will be used for
# all your python files the rest of the semester.

import math

# Initialising Variables
SPL = float(input("Please enter maximum allowable SPL (dB):"))
Pref = float(input("Please enter Reference Pressure (in Pa):"))
v = float(input("Please enter Particle Velocity (in m/s):"))

# Calculating P
num = (SPL**10) * Pref
P = num / 20

# Defining Formula
I = P * v
print('The maximum sound intensity is {0:.2} W/m^2'.format(I))