# Homework 13.1: Python Repetition Flow
# File: HW_13p1_Task2_morepu.py
# Date: 11/27/2023
# By: Pradnyesh More
# Section: 003
# Team: 40

# ELECTRONIC SIGNATURE
# Pradnyesh More

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This programs simulates a BPS reading and tracks the number of times a certain condition occurred


import random

n = int(input("Enter number of Readings you wish to simulate: "))
hypo = 0
hyper = 0
normal = 0

for number in range(0, n, 1):
    flip = random.randint(65, 140)
    print("The Reading Generated is: ", flip)
    if 50 <= flip < 90:
        hypo += 1
    elif 90 <= flip < 120:
        normal += 1
    elif 120 <= flip < 210:
        hyper += 1

print("Number of Normal Readings: {0}\nNumber of Hypotension Reading: {1}\nNumber of Hypertension Reading: {2}".format(normal, hypo, hyper))
