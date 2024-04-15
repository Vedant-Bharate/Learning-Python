# Homework 10 Task 1
# File: HW_10p2_Task1_bharatva.py
# Date: 27 10 20023
# By: Vedant B
# Section: 021
# Team: 359

# ELECTRONIC SIGNATURE
# Vedant Bharate

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This program calculates the angle

# Importing required Libraries
import math

# Getting the inputs from user
Eio=float(input("enter the amplitude of the incident wave"))
N1=float(input("enter the intrinsic impedance of material 1"))
N2=float(input("enter the intrinsic impedance of material 2"))
i=float(input("enter the angle of incidence"))
n1=float(input("enter the refractive index medium 1 "))
n2=float(input("enter the refractive index medium 2 "))

# The math function calculates in different units, so i first changed it to radians first but it will be changed to degrees later before the answer.
T_i=math.pi/180*i

#the following are steps to calculate the theta t
Theta_t = math.asin((n1 / n2) * math.sin(T_i))
Theta_tt = math.degrees(Theta_t)

# I defined a and b to write the two formuals in an easy manner and to avoid errors.
a = math.cos(T_i)
b = math.cos(Theta_t)

# Defining the formula
Eot=((2*N2*a)/((N2*b)+(N1*a)))*Eio
Eor=(((N2*a)-(N1*b))/((N2*a)+(N1*b)))*Eio

# the following will print the answer only till two decimal places.
print("The angle of the transmitted wave = {:.2f}".format(Theta_tt))
print("The amplitude of the reflected wave = {:.2f}".format(Eor))
print("The amplitude of the transmitted wave = {:.2f}".format(Eot))

