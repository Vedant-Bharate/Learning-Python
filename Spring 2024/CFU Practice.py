# File: Example_Additional.py
# Date: 02 January 2024
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
# This program asks the user for a value, unit of value, unit to convert the given value to and in the end asks if user
# wants to convert again (Basically unit convertor)

again = "y"

# Checking if entered unit is correct (Pa or Psi)
while again == "y" or again == "Y":
    # Getting Inputs
    value = float(input("Enter value of pressure: "))
    unit = str(input("Enter units of pressure: "))
    unit_to_convert = str(input("Enter units to convert to: "))

    # Checking if Inputs are Correct
    if (unit == "Pa" or unit == "psi") and (unit_to_convert == "Pa" or unit_to_convert == "psi"):
        # If correct converting
        if unit == "Pa":
            converted_unit = "psi"
            value = value / 6895

        elif unit == "psi":
            converted_unit = "Pa"
            value = value * 6895

        print("The provided value was converted to {0:.5f} {1}".format(value, unit_to_convert))

    else:
        print("Invalid Inputs")

    again = input("Do you want to convert again? (y/n): ")

print("Program Terminated")
