# Homework 13.1: Python Repetition Flow
# File: HW_13p1_Task3_morepu.py
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

# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for
# all your python files the rest of the semester.
# This python program will determine and print the number of
# prime numbers and perfect numbers less than a
# given whole number K

import math

K= int(input("Enter a whole number"))
C1=0
C2=0

for w in range(2,K,1):
    S=0
    n=w
    m=math.ceil(n/2)+1

    for p in range(2,m,1):
        R=(n%p)
        if R==0:
            S=S+p
    if S==0:
        print("The number n= {0} is a prime number".format(n))
        C1=C1+1
    elif S==n-1:
        print("The number n= {0} is a perfect number".format(n))
        C2=C2+1

print("The total number of prime numbers found is C1= {0}".format(C1))
print("The total number of prime numbers found is C2= {0}".format(C2))
