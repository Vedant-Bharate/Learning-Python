# File: ACT_Python_6p1_Team319_bharatva.py
# Date: 25 January 2024
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
# This program reads a list of temperature and then converts in to Fahrenheit and saves it in a list.

# Opening the File to read
temp = open('TempC.txt', 'r')
Lines = temp.readlines()
temp.close()

# Converting String to Float
for i in range(0,len(Lines)):
    Lines[i] = float(Lines[i])

# Converting celsius to Fahrenheit
for j in range(0,len(Lines)):
    Lines[j] = round(Lines[j] * (9/5) + 32)

# Opening a new File and writing list to it
tempf = open('TempF.txt', 'w')
for k in range(0,len(Lines)):
    tempf.write("{0}\n".format(Lines[k]))

tempf.close()
