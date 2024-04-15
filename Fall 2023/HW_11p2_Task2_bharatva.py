# Activity Python: Task 2
# File: HW_11p2_Task2_bharatva
# Date: 11 11 2023
# By: Vedant B
# Section: 021
# Team: 359

# ELECTRONIC SIGNATURE
# Vedant Bharate

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This program determines and prints the nature of public measures to be taken.

# Getting required inputs
s = float(input("Enter the coefficient sigma: "))
mu = float(input("Enter the coefficient mu: "))
g = float(input("Enter the coefficient gamma: "))
d = float(input("Enter the coefficient delta: "))
b1 = float(input("Enter the coefficient beta1: "))
b2 = float(input("Enter the coefficient beta2: "))
a = float(input("Enter the parameter alpha: "))

# Calculating F, R, ac
F = ((d * (b1 * s)) + ((g + mu) * b2)) / ((s + mu) * (g + mu) * mu)
R = (1 - a) * F
ac = 1 - (1 / F)

if R == 1:
    if a < ac:
        print("Endemic state, increase public health measures")
    else:
        print("No change in public health measures")
else:
    if R > 1:
        if a < ac:
            print("Disease expansion state, Increase Public Health Measures")
        else:
            print("No change in public health measures")
    else:
        if a > ac:
            print("Disease Controlled, Decrease Public Health Measures")
        else:
            print("No change in public health measures")
