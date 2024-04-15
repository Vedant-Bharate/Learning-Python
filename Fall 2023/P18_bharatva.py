################################################################################021
#ENED 1100 Exam 3 Problem 18 - Python Repetition
#Please fill out the info below:
#Your Name = Vedant Bharate
#Team Number = 359
#Section Number = 021
################################################################################021

# getting inputs from user:
Y = int(input("Enter Value of Y: "))
N = int(input("Enter Value of N: "))
x = 3

# First WHILE Condition
while N < 100:
    N = int(input("Please re-enter value of N: "))

# Second While Loop:
while Y < N:
    if x < 5:
        x = x + 2
    else:
        x = x - 3

    Y = x**2 + 3*Y

print("X = {0} Y = {1}".format(x, Y))
