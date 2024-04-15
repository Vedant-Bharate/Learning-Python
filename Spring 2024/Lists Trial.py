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


#
import random
N = int(input("How many times do you want to roll? "))
while N <= 0:
    N = int(input("How many times do you want to roll? "))

L = []
count = 0
for i in range(N):
    Dice = random.randint(1, 6) + random.randint(1, 6)
    L.append(Dice)

for j in range(len(L)):
    if L[j] == 7:
        count += 1

print(L)
print(count)
