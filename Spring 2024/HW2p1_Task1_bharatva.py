# File: HW2p1_Task1_bharatva.py
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
# The function generates a frequency distribution of the given data.

import math

# Defining the Function
def HW2p1_Task1_bharatva(a, b, n):
    X = [0.1]
    Y = [0.2]
    for i in range(n - 1):
        Xnext = Y[i]
        X.append(Xnext)
        Ynext = (-b * X[i]) + (a * Y[i]) - (Y[i]) ** 3
        Y.append(Ynext)
    bins = 1 + (round(math.log(n, 2)))
    binwidth = (max(X) - min(X)) / bins
    freq = []
    p = min(X)
    m = p + binwidth
    for j in range(bins):
        z = 0
        for k in X:
            if ((k <= m) and (k >= p)):
                z += 1
        freq.append(z)
        p += binwidth
        m += binwidth
    print("The Frequency Distribution is as follows:")
    return freq
