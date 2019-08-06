from random import randint


def dice_rolls(dice_num: int = 1, die_size: int = 6):
    """
    Roll a die for a given number of times only once.
    :param dice_num: number of dice to roll
    :param die_size: number of faces on the die
    :return: rolls: list of dice rolls
    """

    # Check if die_size is in expected range.
    if die_size not in {4, 6, 10, 12, 20, 100}:
        raise ValueError

    # Roll one die for each diceNum of size diceSize.
    rolls = []
    for n in range(dice_num):
        # Append each roll to rollList.
        rolls.append(randint(1, die_size))
    return rolls


def dice_roll_suite(dice_num: int = 1, die_size: int = 6,
                    number_of_rolls: int = 1):
    """
    Roll a die for a given number of times at least once.
    :param dice_num: number of dice to roll
    :param die_size: number of faces on the die
    :param number_of_rolls: number of times to roll dice
    :return: rolls: dictionary of list of dice rolls
    """

    # Check if die_size is in expected range.
    if die_size not in {4, 6, 10, 12, 20, 100}:
        raise ValueError

    # Create dictionary of each set of rolls.
    rolls = {}
    # Iterate over each roll.
    for roll in range(number_of_rolls):
        # Store each roll in our rolls dictionary.
        rolls[roll+1] = dice_rolls(dice_num, die_size)
    # Return dictionary of each set of rolls.
    return rolls
