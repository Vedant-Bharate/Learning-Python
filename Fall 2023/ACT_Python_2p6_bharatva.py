# Activity Python 1: Task 6
# File: ACT_Python_HeaderTemplate_Team359_bharatva.py
# Date: 02 11 2023
# By: Vedant B
# Section: 021
# Team: 359

# ELECTRONIC SIGNATURE
# Vedant Bharate

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This program analyses the temperature and pressure of a reactor and outputs the status

# Importing required libraries
import math
import random

# Getting the input from user and computer
cc = random.randint(1,3)
uc = int(input("Enter your choice (rock - 1, paper - 2, scissor - 3)"))

# Comparing
if (cc == 1 and uc == 1) or (cc == 2 and uc == 2) or (cc == 3 and uc == 3):
    print("TIE")
elif (cc == 1 and uc == 3) or (cc == 2 and uc == 1) or (cc == 3 and uc == 2):
    print("Computer WINS")
else:
    print("User WINS")