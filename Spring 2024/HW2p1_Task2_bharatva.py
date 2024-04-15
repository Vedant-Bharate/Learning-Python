# File: HW2p1_Task2_bharatva.py
# Date: 19 January 2024
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
# This program defines three new functions and calls them.

# Function for
####################################################################
def Happy(num):
    count = 0
    while num != 1 and count < 100:
        count = count + 1
        num0 = 0
        for digit in str(num):
            num0 = num0 + (int(digit)) ** 2
        num = num0
    return num == 1


#####################################################################
def Perfect(num):
    divisors = 0
    for i in range(1, num):
        if num % i == 0:
            divisors = divisors + i
    return divisors == num


######################################################################
def Narcissistic(num):
    narcis = 0
    num_str = str(num)
    num_digits = len(num_str)
    for digit in num_str:
        narcis = narcis + (int(digit)) ** num_digits

    return narcis == num


######################################################################
##############Start your script here################################
####################################################################

# Get the input from the user.
N = int(input("Enter a whole number N: "))

# Create a list to store the numbers found.
numbers_found = []
# Create a list to store the corresponding number types.
number_types = []

# Iterate over the numbers from 1 to N and check if they are happy, perfect, or narcissistic.
for i in range(1, N + 1):
    numbers_found.append(i)
    num_type = ""

    # Check if the number is happy.
    if Happy(i):
        num_type = "h"

    # Check if the number is narcissistic.
    elif Narcissistic(i):
        num_type = num_type + "n"

    # Check if the number is perfect.
    elif Perfect(i):
        num_type = num_type + "p"

    else:
        num_type = num_type + "neither a Happy, Narcissistic or a Perfect"

    # Printing the lists
    number_types.append(num_type)
    print(str(numbers_found[i - 1]) + " is " + str(number_types[i - 1]))
