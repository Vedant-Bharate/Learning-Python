# Activity Python 1: Task 3
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

# This program calculates force, and distance of spring according to Hooke's Law

# Importing required libraries
import math

# Getting the inputs
K1 = float(input('Please enter the spring constant, K1 (N/m): '))
K2 = float(input('Please enter the spring constant, K2 (N/m): '))
Ft = float(input('Please enter the Total Force (N): '))
CS = input('Please enter the configuration of the spring (s/p): ')

#   Checking if the inputs are valid or invalid
if K1 < 0 or K2 < 0 or Ft < 0:
    print('Invalid Inputs.')

# If inputs are valid, calculating the Distance spring is compressed or streched (X)
else:
# If Config is parallel
    if CS == 'p':
        Keq = K1 + K2
        X1 = Ft / Keq
        X2 = X1
        F1 = K1 * X1
        F2 = K2 * X2
        Xt = X1 = X2
        print(f"Keq = {Keq:.2f}\n X1 = {X1:.2f}\n X2 = {X2:.2f}\n F1 = {F1:.2f}\n F2 = {F2:.2f}\n X total = {Xt:.2f}")

# If config is series
    else:
        Keq = (1 / K1) + (1 / K2)
        Keq = 1 / Keq
        X1 = Ft / K1
        X2 = Ft / K2
        F1 = K1 * X1
        F2 = K2 * X2
        Xt = X1 + X2
        print(f"Keq = {Keq:.2f}\n X1 = {X1:.2f}\n X2 = {X2:.2f}\n F1 = {F1:.2f}\n F2 = {F2:.2f}\n X total = {Xt:.2f}")
