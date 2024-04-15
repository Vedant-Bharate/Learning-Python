# File: Projectile_bharatva.py
# Date: 12 February 2024
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
# This program creates a function that calculates the time of flight of a projectile.

# importing libraries
import math


# defining function
def Projectile_bharatva():
    # Getting inputs from user:
    angle = float(input("Please enter the value for theta (degrees): "))
    min_velocity = float(input("Please enter the minimum velocity (m/s): "))
    max_velocity = float(input("Please enter the maximum velocity (m/s): "))
    spacing = (max_velocity - min_velocity) / 10
    initial_velocity = max_velocity - min_velocity
    list = []

    # converting angle from degree to radian:
    angle = angle * (math.pi / 180)

    # Checking if the max_velocity is greater than min_velocity, else ask for input again
    while min_velocity > max_velocity:
        max_velocity = float(input("Please enter the maximum velocity (m/s): "))

    # Creating for loop:
    for i in range(0, 11):
        Timpact = (2 * initial_velocity * math.sin(angle)) / 9.81
        initial_velocity += spacing
        # Adding values to list
        list.append(Timpact)

    # Printing the list
    print(list)
    return list

Projectile_bharatva()