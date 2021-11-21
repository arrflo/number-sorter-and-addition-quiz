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
    _result = int (addend1 + augend1)
    return _result

def resultSummary(_score):
    print (f"You got {_score} out of 10 questions correct.")

def pointing ():
    _right = int (1)
    _wrong = int (0)
    return _right, _wrong

def qOne():
    if firstQ == resultAB:
        return right
    else: return wrong
def qTwo():
    if secondQ == resultCD:
        return right
    else: return wrong
def qThree():
    if thirdQ == resultEF:
        return right
    else: return wrong
def qFour():
    if fourthQ == resultGH:
        return right
    else: return wrong
def qFive():
    if fifthQ == resultIJ:
        return right
    else: return wrong
def qSix():
    if sixthQ == resultKL:
        return right
    else: return wrong
def qSeven():
    if seventhQ == resultMN:
        return right
    else: return wrong
def qEight():
    if eighthQ == resultOP:
        return right
    else: return wrong
def qNine():
    if ninthQ == resultQR:
        return right
    else: return wrong
def qTen():
    if tenthQ == resultST:
        return right
    else: return wrong


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

# result score
right, wrong = pointing ()
A = qOne ()
B = qTwo ()
C = qThree ()
D = qFour ()
E = qFive ()
F = qSix ()
G = qSeven ()
H = qEight ()
I = qNine ()
J = qTen ()

#other
score = A + B + C + D + E + F + H + J
resultSummary (score)