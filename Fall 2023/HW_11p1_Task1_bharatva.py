# Activity Python: Task 1
# File: HW_11p2_Task1_bharatva
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

# This program based on the user inputs, the program should output the exercise intensity level
# and the calories burned per hour

# Getting required inputs
age = float(input("Enter the user age in years: "))
weight = float(input("Enter the user weight in pounds: "))
CHR = float(input("Enter the user current heart rate in beats/minute: "))
m = input("Enter the type of machine (auto/manual): ")

if m == "auto" or m == "manual":
    if m == "auto":
        MHR = 206 - (0.88 * age)
        CB = 60 * (((age * 0.2017) + (weight * 0.09036) + (CHR * 0.6309) - 55.0969) / 4.184)
    else:
        MHR = 205.8 - (age * 0.685)
        CB = 60 * (((age * 0.074) - (weight * 0.05741) + (CHR * 0.4472) - 20.4022) / 4.184)

# Checking Exercise Intensity Level
    if CHR < (0.6*MHR):
        EIL = "Below Level"
    elif CHR < (0.7*MHR):
        EIL = "Weight Loss"
    elif CHR < (0.8*MHR):
        EIL = "Cardio"
    elif CHR < (0.9*MHR):
        EIL = "Anaerobic (Hardcore)"
    else:
        EIL = "Above Level"

# Printing Outputs
    print('Calories burnt per hour is: {0:.2f}, for an activity level of: {1}'.format(CB, EIL))

else:
    print("Invalid Input")
