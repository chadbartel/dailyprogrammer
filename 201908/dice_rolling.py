from random import randint


def diceRolls(diceNum, dieSize):
    # Create list of dice rolls.
    rollList = []
    # Roll one die for each diceNum of size diceSize.
    for n in range(diceNum):
        # Append each roll to rollList.
        rollList.append(randint(1, dieSize))
    return rollList


def diceRollSuite(diceNum, dieSize, rollNum = 1):
    # Create dictionary of values, in case rollNum > 1.
    rolls = {}
    # If rollNum value doesn't change.
    if rollNum == 1:
        # Roll x dice 1 time.
        return diceNum * randint(1, dieSize)
    # If rollNum value changes.
    else:
        # Since rollNum > 1, iterate through each roll.
        for r in range(rollNum):
            # Store each roll in our rolls dictionary.
            rolls[r+1] = diceRolls(diceNum, dieSize)
        # Return a dictionary of multiple rolls.
        return rolls
