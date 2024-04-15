# Homework 10 Task 1
# File: HW_10p2_Task1_bharatva.py
# Date: 27 10 2005
# By: Vedant B
# Section: 021
# Team: 359

# ELECTRONIC SIGNATURE
# Vedant Bharate

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This program calculates the Interest Rate, Final Amount, and Interest Earning.

# Importing required Libraries
import math

# Initialising Variable and getting the input
P = float(input("Enter original Principal Sum: "))
X = float(input("Annual Interest Factor: "))
n = float(input("Compunding frequency: "))
t = float(input("Overall length of interest: "))

# Defining Formula
r = (1/n**2) * abs(math.sin(X) / X)
A = P * ((1 + r)**(n * t))
I = A - P

# Outputs:
print('The interest rate is: {0:.4f}\nPrincipal Amount is: ${1:.2f}\nFinal Amount is: ${2:.2f}\nInterest Earning is: ${3:.2f}'.format(r, P, A, I))
