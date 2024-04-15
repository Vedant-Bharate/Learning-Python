# File: HW Task 2.py
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
# This program stores the questions in a text file.

import random
n = int(input("How many questions to store in a new file? "))
x = open('TeamQuestion.txt', 'r')
questions = x.readlines()
x.close()
questionlist = []
for i in range(n):
    answer = "n"
    while(answer=="n"):
        r = random.randint(0, len(questions))
        print(questions[r])
        answer = input("Keep this question? (Enter y or n): ")
        if(answer=="y"):
            questionlist.append(questions[r])
y = open("QuestionsToAsk.txt", "w")
for j in questionlist:
    y.write(j)
y.close()
