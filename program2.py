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

def getQuestions (augend, addend):
    _question = int(input (f"{augend} + {addend} ="))
    return _question

def correctAnswers (augend1, addend1):
    _result = int (augend1 + addend1)
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

def rightAnswer ():
    print ("That's right! You're a Genius!")

def wrongAnswer (_answer):
    print (f"The correct answer is, {_answer}. Don't worry! you'll get it next time.")


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

# 10 questions

header ()

firstQ = getQuestions (a,b)
if firstQ == resultAB:
     rightAnswer()
else: wrongAnswer (resultAB)

secondQ = getQuestions (c,d)
if secondQ == resultCD:
     rightAnswer()
else: wrongAnswer (resultCD)

thirdQ = getQuestions (e,f)
if thirdQ == resultEF:
     rightAnswer()
else: wrongAnswer (resultEF)

fourthQ = getQuestions (g,h)
if fourthQ == resultGH:
     rightAnswer()
else: wrongAnswer (resultGH)

fifthQ = getQuestions (i,j)
if fifthQ == resultIJ:
     rightAnswer()
else: wrongAnswer (resultIJ)

sixthQ = getQuestions (k,l)
if sixthQ == resultKL:
     rightAnswer()
else: wrongAnswer (resultKL)

seventhQ = getQuestions (m,n)
if seventhQ == resultMN:
     rightAnswer()
else: wrongAnswer (resultMN)

eighthQ = getQuestions (o,p)
if eighthQ == resultOP:
     rightAnswer()
else: wrongAnswer (resultOP)

ninthQ = getQuestions (q,r)
if ninthQ == resultQR:
     rightAnswer()
else: wrongAnswer (resultQR)

tenthQ = getQuestions (s,t)
if tenthQ == resultST:
     rightAnswer()
else: wrongAnswer (resultST)


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
score = A + B + C + D + E + F + G + H + I + J
resultSummary (score)