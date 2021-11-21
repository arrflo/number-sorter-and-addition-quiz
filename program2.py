# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random

def getRandomNumbers ():
    randomm = random.randint(0, 99)
    return randomm

def header ():
    print ("Addition Quiz")
    print ("Answer the following questions correctly.")

def getQuestions (addend, augend):
    _question = int(input (f"{addend} + {augend} ="))
    return _question

def correctAnswers (addend1, augend1):
    _result = addend1 + augend1
    return _result

# variables for 20 random numbers
a = getRandomNumbers ()
b = getRandomNumbers ()
c = getRandomNumbers ()
d = getRandomNumbers ()
e = getRandomNumbers ()
f = getRandomNumbers ()
g = getRandomNumbers ()
h = getRandomNumbers ()
i = getRandomNumbers ()
j = getRandomNumbers ()
k = getRandomNumbers ()
l = getRandomNumbers ()
m = getRandomNumbers ()
n = getRandomNumbers ()
o = getRandomNumbers ()
p = getRandomNumbers ()
q = getRandomNumbers ()
r = getRandomNumbers ()
s = getRandomNumbers ()
t = getRandomNumbers ()

# 10 questions
header ()
firstQ = getQuestions (a,b)
secondQ = getQuestions (c,d)
thirdQ = getQuestions (e,f)
fourthQ = getQuestions (g,h)
fifthQ = getQuestions (i,j)
sixthQ = getQuestions (k,l)
seventhQ = getQuestions (m,n)
eighthQ = getQuestions (o,p)
ninthQ = getQuestions (q,r)
tenthQ = getQuestions (s,t)

# Answer Key
resultAB = correctAnswers (a,b)
resultCD = correctAnswers (c,d)
resultEF = correctAnswers (e,f)
resultGH = correctAnswers (g,h)
resultIJ = correctAnswers (i,j)
resultKL = correctAnswers (k,l)
resultMN = correctAnswers (m,n)
resultOP = correctAnswers (o,p)
resultQR = correctAnswers (q,r)
resultST = correctAnswers (s,t)

