from random import randint

GameLevel = {"E": 4, "M": 5, "H": 6, "V": 8, "I": 10}
Answer = {"Y", "N"}
Level = "E"
Mode = "N"


# if number contains same digits return true, else false
def IsContainsDuplicates(number):
    for xK, xV in enumerate(list(str(number))):
        for yK, yV in enumerate(list(str(number))):
            if xK != yK and xV == yV:
                return True
    return False


# generate a new number that will be guessed
def GenerateGuessNumber(digitCount, allowSameDigit):
    minValue = (10 ** (digitCount - 1))
    maxValue = (10 ** digitCount - 1)
    guessNumber = randint(minValue, maxValue)
    if allowSameDigit == "N" and IsContainsDuplicates(guessNumber):
        guessNumber = GenerateGuessNumber(digitCount, allowSameDigit)
    return guessNumber


# validate the guess number if it fits necessary conditions
def ValidateGuessNumber(guessNumber, digitCount):
    try:
        guessNumber = int(guessNumber)
        if guessNumber < 10 ** (digitCount - 1) or guessNumber > 10 ** digitCount - 1:
            print("ERROR: Please enter a number only {0} digits.".format(digitCount))
            return False

        if Mode == "N" and IsContainsDuplicates(guessNumber):
            print("ERROR: Duplicate digits are not allowed.")
            return False
        return True
    except ValueError:
        print("ERROR: Please enter a valid number.")
        return False


# gets user's guess number as an input
def MakeGuess(digits):
    guess = input("Make your guess: ")
    if ValidateGuessNumber(guess, digits):
        return int(guess)
    else:
        return -1


# compares two numbers (user guess and number to found)
def CompareGuess(currentGuess, actualNumber):
    currentGuessDigits = list(str(currentGuess))
    actualNumberDigits = list(str(actualNumber))
    knownNumberCount = correctPlaces = 0
    foundIndex = 0

    # first check if any numbers are in the correct place
    index = 0
    while index < len(currentGuessDigits):
        if currentGuessDigits[index] == actualNumberDigits[index]:
            correctPlaces += 1
            knownNumberCount += 1
            actualNumberDigits[index] = -1
            currentGuessDigits[index] = -1
        index += 1

    for currIndex, currValue in enumerate(currentGuessDigits):
        if currValue == -1:
            continue
        isKnown = False
        for actIndex, actValue in enumerate(actualNumberDigits):
            if actValue == -1:
                continue
            if actValue == currValue:
                if not isKnown:
                    isKnown = True
                    knownNumberCount += 1
                    foundIndex = actIndex
        if isKnown:
            actualNumberDigits[foundIndex] = -1
    print(">>> Your Guess: {0}, Found: {1}, Correct Place: {2}".format(currentGuess, knownNumberCount, correctPlaces))


# provides a level selection option
def SelectLevel():
    print("E=Easy(4), M=Medium(5), H=Hard(6), V=Veteran(8), I=Impossible(10)")
    global Level
    Level = input("Please select your level: ").upper()
    if Level not in GameLevel:
        print("ERROR: Invalid selection! Please try again.")
        Level = SelectLevel()
    return Level


# provides a mode selection option
def SelectMode():
    print("Do you want to enable 'Allow Same Digits' option?")
    print("Y=Yes, N=No")
    global Mode
    Mode = input("Please select your answer: ").upper()
    if Mode not in Answer:
        print("ERROR: Invalid selection! Please try again.")
        Mode = SelectMode()
    return Mode


# plays the game
def PlayGame():
    level = SelectLevel()
    allowSameDigit = SelectMode()

    digits = GameLevel[level]
    guessNumber = GenerateGuessNumber(digits, allowSameDigit)
    # print("Number to guess: {0}".format(guessNumber))
    currentGuess = 0
    guessCount = 0

    while guessNumber != currentGuess:
        currentGuess = MakeGuess(digits)
        guessCount += 1
        if currentGuess == -1:
            continue
        else:
            CompareGuess(currentGuess, guessNumber)
    print("Hooray! You did it on {0} tries...".format(guessCount))


PlayGame()
