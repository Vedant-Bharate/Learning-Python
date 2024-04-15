# File: Example_Additional.py
# Date: 02 January 2024
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
#

# This model aims to predict the distance the robot will be off if asked to start at location A
# and then go to a box anywhere in the facility.

# Getting Inputs from User
distance_i = float(input("Enter Initial Forward Movement Distance(inches): "))
turn = input("Does the robot need to turn to reach destination (Y/N): ")

# If Robot needs to turn, getting additional inputs
if turn == "Y" or turn == "Yes" or turn == "y":
    num_turns = int(input("How many turns would the robot need to take? "))
    # Getting number of terms required
    for i in range(num_turns):
        angle = float(input("For turn {0} Enter the angle in degrees: ".format(i+1)))
        distance = float(input("After turn {0} Enter the distance robot needs to move: ".format(i+1)))
        print("ERROR CALCULATING")

# If Robot doesn't need to turn calculating and printing error
else:
    print("ERROR CALCULATING")
