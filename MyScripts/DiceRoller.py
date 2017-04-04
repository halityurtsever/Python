# import randint from random to produce random dice numbers
from random import randint

# define a tuple for dice faces. tuples are immutable. they cannot be changed.
diceFaces = (1, 2, 3, 4, 5, 6)


# random dice number selector. returns a couple of dice result.
def SelectRandomDiceScore():
    diceRoll = lambda x: randint(min(x), max(x))
    return [diceRoll(diceFaces), diceRoll(diceFaces)]


# roll a dice as many as passed to the method
def DiceRoller(rollCount):
    rollList = []
    while rollCount > 0:
        rollResult = SelectRandomDiceScore()
        rollList.append(rollResult)
        rollCount -= 1
    return rollList


# print roll results to console
def PrintRollResults(results):
    lineNumber = 1
    for result in results:
        # result list contains type of string because it has been read from a file
        # that's why we convert items from strings to int in the list        
        result = list(map(int, result))
        if result[0] == 6 and result[1] == 6:
            message = " Hooray! You are the best..."
        elif result[0] == 1 and result[1] == 1:
            message = " Booooo! You are the worst..."
        elif result[0] == result[1]:
            message = " Whoooo! It is a double..."
        else:
            message = ""
        print("Line {3}: {0} - {1}{2}".format(result[0], result[1], message, lineNumber))
        lineNumber += 1


# save roll results to a file
def SaveRollResults(filename, rollResults):
    with open(filename, "a") as file:
        for result in rollResults:
            file.write("{0} - {1}\n".format(result[0], result[1]))


# read roll results from a file
def ReadRollResults(filename):
    rollList = []
    with open(filename, "r") as file:
        for line in file.read().splitlines():
            rollList.append(line.split(" - "))
    return rollList


# filter results considering to passed function
def FilterResults(func, results):
    return len(list(filter(func, results)))


# count each single dice face
def CountEachSingleDiceFace(face, rollResults):
    single = lambda x: x[0] == face or x[1] == face
    double = lambda x: x[0] == face and x[1] == face
    singleCount = FilterResults(single, rollResults)
    doubleCount = FilterResults(double, rollResults)
    return singleCount + doubleCount


# analyze dice roll results
def AnalyzeResults(filename):
    print("#######################################")
    print("ANALYZE RESULTS")
    print("#######################################")

    # read all dice roll results from file
    rollResults = ReadRollResults(filename)

    # roll count
    print("Roll Count: %d" % (len(rollResults)))

    # best score count (6-6)    
    best = lambda x: x[0] == "6" and x[1] == "6"
    bestCount = FilterResults(best, rollResults)
    print("Best Score Count (6-6): %d" % bestCount)

    # worst score count (1-1)    
    worst = lambda x: x[0] == "1" and x[1] == "1"
    worstCount = FilterResults(worst, rollResults)
    print("Worst Score Count (1-1): %d" % worstCount)

    # double score count    
    double = lambda x: x[0] == x[1]
    doubleCount = FilterResults(double, rollResults)
    print("Double Score Count (x-x): %d" % doubleCount)

    # count of single dice faces    
    for x in diceFaces:
        print("Count of %ds: %d" % (x, CountEachSingleDiceFace(str(x), rollResults)))


SaveRollResults("dice_roll_results.txt", DiceRoller(10))
PrintRollResults(ReadRollResults("dice_roll_results.txt"))
AnalyzeResults("dice_roll_results.txt")
