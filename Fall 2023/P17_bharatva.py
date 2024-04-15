################################################################################021
#ENED 1100 Exam 3 Problem 17 - Python Conditional
#Please fill out the info below:
#Your Name = Vedant Bharate
#Team Number = 359
#Section Number = 021
################################################################################021
import sys
# Getting inputs from the User
speed = int(input("Enter speed of vehicle (m/s): "))
Tcar = input("Enter type of Vehicle (car/truck): ")

# If speed is greater than 85 calling police:
if speed > 85:
    print("Police Interception URGENT")
elif Tcar == "car":
    if speed <= 65:
        print("Withing Limit")
    elif speed > 65:
        print("Speeding")
elif Tcar == "truck":
    if speed <= 55:
        print("Withing Limit")
    elif speed > 55:
        print("Speeding")
