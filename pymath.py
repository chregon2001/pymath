# Christian Egon Sørensen© 2019, MIT License
from random import randint
from pprint import pprint
import math
import sys
import json
import os
import time
from prettytable import PrettyTable
from argparse import ArgumentParser

parser = ArgumentParser()
# parser.add_argument("-f", "--file", dest="filename",
#                     help="write report to FILE", metavar="FILE")
# parser.add_argument("-q", "--quiet",
#                     action="store_false", dest="verbose", default=True,
#                     help="don't print status messages to stdout")
parser.add_argument("-d", "--daily", default=False,
                    help="Runs a daily string of excersises")
parser.add_argument('-n',"--number-of-questions", default=10, help="How many questions to go through")

args = parser.parse_args()

#! ROADMAP
# COMPLETING THE SQUARE
#? Daily mode, making all decisions by predetermined info # DONE
#? = MATHQ, raing that automatically adjust questinons hardness # DONE
# integrals
# Differenntial
# matrix multiplication
# vetor addition
# common sinus, cosin, tan, trig identities questions
# Timer
# Percent color gradient
# Amount of correct and incorrect listed

answers = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def intro():    
    choices = set(["a","s","as","m","d","mt"])
    choice = input("What category would you like?{A,S,AS,M,D,MT} ")
    if(choice not in choices):
        print("Input not recognized")
        return False
    return choice
    
def floatRound2prec(n):
    n = n * 100
    n = int(n)
    n = n / 100
    return n

def generateQuestion(o,l,u):
    #O operator
    #l lower bound
    #u upper bound
    a = randint(l, u)
    b = randint(l,u)
    if(o=='a'):
        return ( str(a) + " + " + str(b), a+b, o )
    if(o=='s'):
        return ( str(a) + " - " + str(b), a-b , o)
    if(o=='as'):
        if(randint(0,1)):
            return ( str(a) + " - " + str(b), a-b , o)
        else:
            return ( str(a) + " + " + str(b), a+b , o)
    if(o=="m"):
        return ( str(a) + " * " + str(b), a*b , o)
    if(o=="d"):
        return ( str(a) + " / " + str(b), a/b , o)

def addAnswer(correct, q, a):
    # Correct, bool for was it true
    # q, the question tuple
    answers.append([correct,q, a])

def displayCorrectness(answers):
    # Just displays correctness nicely
    print("\n")
    print("+"*20)
    print("\n")
    for i in answers:
        print(str(i[2]) + " was "+correctnessToString(i[0]) + " to " +i[1][0] + ", it was " + str(i[1][1]))
    accum = 0
    for i in answers:
        if(i[0]):
            accum += 1
        else:
            pass
    print(str(accum/len(answers)*100) + "% correct!")
    print("\n")
    print("+"*20)


def correctnessToString(cnes):
    if(cnes):
        return (bcolors.OKGREEN + "Correct" + bcolors.ENDC)
    else:
        return (bcolors.FAIL+"Not correct"+bcolors.ENDC)

def isCorrectFloat(a, g):
    os.system('clear')
    if(floatRound2prec(float(a)) == floatRound2prec(g[1])):
        addAnswer(True, g, a)
        return (bcolors.OKBLUE + "correct" + bcolors.ENDC)
    else:
        addAnswer(False, g, a)
        return (bcolors.FAIL + "incorrect, it was " + str(g[1]) + " (after rounding" + str(floatRound2prec(g[1])) +" ) " + bcolors.ENDC)

def isCorrectInt(a, g):
    os.system('clear')
    if(int(a) == g[1]):
        addAnswer(True, g, a)
        return (bcolors.OKBLUE + "correct" + bcolors.ENDC)
    else:
        addAnswer(False, g, a)
        return (bcolors.FAIL + "incorrect, it was " + str(g[1]) + bcolors.ENDC)

def makeQuestionInt(g):
    a = input("What is " + g[0] + "? ")
    try:
        val = int(a)
    except ValueError:
        print("Input not recognized")
        return makeQuestionInt(g)
    return a

def makeQuestionFloat(g):
    a = input("What is " + g[0] + "? ")
    try:
        val = float(a)
    except ValueError:
        print("Input not recognized")
        return makeQuestionFloat(g)
    return a

def chooseBridge(choice,rating={}):
    #Refactor
    ua = 10
    us = 10
    uas = 10
    um = 10
    ud = 10
    umt = 10
    if(args.daily!=False):
        if "a" in rating:
            ua = 10 + rating["a"]
        if "s" in rating:
            us = 10 + rating["s"]
        if "as" in rating:
            uas = 10 + rating["as"]
        if "m" in rating:
            um = 10 + rating["m"]
        if "d" in rating:
            ud = 10 + rating["d"]
        if "mt" in rating:
            umt = 10 + rating["mt"]
    if(choice.lower()=="a"): # ADDITION
        g = generateQuestion("a",0,ua)
        a = makeQuestionInt(g)
        print(isCorrectInt(a,g))
    elif(choice.lower()=="s"): # SUBTRACTION
        g = generateQuestion("s",0,us)
        a = makeQuestionInt(g)
        print(isCorrectInt(a,g))
    elif(choice.lower()=="as"): # ADDITION- SUBTRACTION
        g = generateQuestion("as",0,uas)
        a = makeQuestionInt(g)
        print(isCorrectInt(a,g))
    elif(choice.lower()=="m"): # MULTIPLICATION
        g = generateQuestion("m",0,um)
        a = makeQuestionInt(g)
        print(isCorrectInt(a,g))
    elif(choice.lower()=="d"): # DIVISION
        g = generateQuestion("d",1,ud)
        a = makeQuestionFloat(g)
        print(isCorrectFloat(a,g))
    elif(choice.lower()=="mt"): #MULTIPLICATION TABLE
        multtable(1,umt,10)


def multtable(l,u,n):
    
    for i in range(1,10+1):
        for k in range(0,2):
            os.system('clear')
            print("")
            for j in range(0,10+1):
                printMultTable(i,10)
                a = input("What is " + str(i) + " * " + str(j) + " = ")
                os.system('clear')
                if(i*j==int(a)):
                    print(bcolors.OKGREEN + "Correct" + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + "Wrong, the answer is " + str(i*j) + bcolors.ENDC)
        os.system('clear')
        print("")
        for k in range(0,15):
            b = randint(l,u)
            a = input("What is " + str(i) + " * " + str(b) + " = ")
            os.system('clear')
            if(i*b==int(a)):
                print(bcolors.OKGREEN + "Correct"+ bcolors.ENDC)
            else:
                print(bcolors.FAIL +"Wrong, the answer is " + str(i*b)+ bcolors.ENDC)
def printMultTable(x,n):
    table=[]
    mark=[]
    i = 1
    print("Multiplication table for " + str(x))
    for i in range(1,n+1):
        mark.append(1*i)
    for i in range(1,n+1):
        table.append(x * i)
    t = PrettyTable(mark)
    
    t.add_row(table)
    print(t)

def newScore(answers):
    accum = 0
    recomend = 0
    for i in answers:
        if(i[0]):
            accum += 1
        else:
            pass
    rating = accum/len(answers)
    if(rating==0):
        recomend = -2
    elif(rating<0.25):
        recomend = -1
    elif(rating<0.50):
        recomend = 0
    elif(rating<0.75):
        recomend = 0
    elif((rating>=0.75) and (rating<90)):
        recomend = +1
    elif(rating>=0.90):
        recomend = +2
    return recomend

def calculateRecommendedChange(answers):
    table = {}
    rating = {}
    for i in answers:
        try:
            table[i[1][2]].append(i)
        except KeyError as e:
            table[i[1][2]] = [i]
    for key in table:
        score = newScore(table[key])
        rating[key] = score
    return rating

def applyChange(rating,changes):
    rating = rating
    changes = changes
    for chankey in changes:
        try:
            print()
            rating[chankey] += changes[chankey]
        except KeyError as e:
            rating[chankey] = changes[chankey]
    return rating

def loadRating():
    try:
        with open('data.json', 'r') as fp:
            data = json.load(fp)
            return data
    except FileNotFoundError as identifier:
        saveRating({})
        return {}
    

def saveRating(rating):
    with open('data.json', 'w') as fp:
        json.dump(rating, fp)

os.system('clear')
if args.daily == False:
    er = intro()
    if(er == False):
        # Todo, ask again
        print("HALTING AND CATCHING FIRE")
        sys.exit()
    choice= er
    amo = args.number_of_questions
    for i in range(0,amo):
        chooseBridge(choice)
    displayCorrectness(answers)
else:
    prescription = args.daily.split(',')
    rating = loadRating()
    print("")
    for p in prescription:
        if(p!="mt"):
            for i in range(0,args.number_of_questions):
                chooseBridge(p,rating=rating)
        else:
            chooseBridge(p,rating=rating)
    displayCorrectness(answers)

    changes = calculateRecommendedChange(answers)
    newrating = applyChange(rating,changes)
    saveRating(newrating)
