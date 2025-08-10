# run py code: CTRL + R
# format document by pep8: SHIFT + ALT + F

import random

number1 = 0
number2 = 1

#name = input("Please provide your name: ")
goodAnswers = 0
numberOfQuestions = 10

for x in range(numberOfQuestions):

    resolut = None

    while True:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 20)
        
        if (number1 % number2) == 0:
            break

    question = ("Please provide resoult division of ") + str(number1) + (" and ") + str(number2) + (": ")

    while resolut is None: 
        try:
            resolut = int(input(question))
        except ValueError:
            continue

    if resolut == (number1/number2):
        goodAnswers = goodAnswers + 1
        print ("\x1b[6;30;42m" + "Good, you are erning star: *" + "\x1b[0m")
    else:
        print ("\x1b[6;30;41m" + "Oh no, you made a mistake :-(" + "\x1b[0m")

if goodAnswers == numberOfQuestions:
    print ("Great job! You are the best! You can eat icecreams now ;-) You have earned:", goodAnswers, "of", numberOfQuestions, "stars")
if goodAnswers < numberOfQuestions and goodAnswers >= numberOfQuestions/2:
    print ("Not bad but also not perfect. Keep trying ;-) You have earned:", goodAnswers, "of", numberOfQuestions, "stars")
if goodAnswers > 0 and goodAnswers < numberOfQuestions/2:
    print ("Keep learning and try again. You have earned:", goodAnswers, "of", numberOfQuestions, "stars")
if goodAnswers == 0:
    print ("Better go back to learn. YYou have earned:", goodAnswers, "of", numberOfQuestions, "stars")

