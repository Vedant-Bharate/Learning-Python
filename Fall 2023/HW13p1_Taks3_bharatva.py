# Activity Python: Task 3
# File: HW_13p1_Task3_bharatva
# Date: 25 11 2023
# By: Vedant B
# Section: 021
# Team: 359

# ELECTRONIC SIGNATURE
# Vedant Bharate

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# This program determines and print the number of prime numbers and perfect numbers less than a given whole number K

# Importing Required Libraries
import math

# Getting required inputs
K = int(input("Enter a whole number 'K': "))
C1 = 0
C2 = 0

# Initiating FOR Loop
for W in range(2, K, 1):
    S = 0
    n = W
    m = math.ceil(n / 2) + 1

    # Initiating Second For Loop
    for p in range(2, m, 1):
        R = n % p
        if R == 0:
            S = S + p
    if S == 0:
        print("The number n = {0} is prime".format(n))
        C1 = C1 + 1
    elif S == n - 1:
        print("The number n = {0} is perfect".format(n))
        C2 = C2 + 1

print("The total number of prime numbers found is C1 =", C1)
print("The total number of perfect numbers found is C2 =", C2)
