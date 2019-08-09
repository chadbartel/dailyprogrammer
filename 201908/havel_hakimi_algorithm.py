"""
Challenge: Given a sequence of answers to the question,
    "How many people at the party have have you met before tonight?"
apply the Havel-Hakimi algorithm to determine whether or not it's possible
that everyone was telling the truth.
    1. Remove all 0's from the sequence (i.e. warmup1).
    2. If the sequence is now empty (no elements left), stop and return true.
    3. Sort the sequence in descending order (i.e. warmup2).
    4. Remove the first answer (which is also the largest answer, or tied for
        the largest) from the sequence and call it N. The sequence is now 1
        shorter than it was after the previous step.
    5. If N is greater than the length of this new sequence (i.e. warmup3),
        stop and return false.
    6. Subtract 1 from each of the first N elements of the new sequence
        (i.e. warmup4).
    7. Continue from step 1 using the sequence from the previous step.
Challenge by: u/Cosmologicon

Author: Chad Bartel
Date:   8/8/2019
"""


def havel_hakimi_algorithm(l: list):
    """
    Apply the Havel-Hakimi algorithm to a given list of integers.

    :param l: list of integers
    :return result: True/False
    """

    # Copy list to new variable.
    l_copy = l.copy()
    print(l_copy)

    # Loop through steps until True or False is reached.
    result = None
    while result is None:
        # Remove all 0's from 'l'.
        l_copy = [x for x in l_copy if x != 0]
        print(l_copy)

        # If 'l' is empty, return True.
        if len(l_copy) < 1:
            result = True
            print(result)
            break

        # Sort 'l' in descending order.
        l_copy.sort(reverse=True)
        print(l_copy)

        # Remove the first element in 'l' and assign that value to 'n'.
        l_copy.reverse()
        n = l_copy.pop()
        l_copy.reverse()
        print(l_copy)

        # If 'n' is greater than length 'l', return False.
        if n > len(l_copy):
            result = False
            print(result)
            break

        # Remove 1 from the first 'n' elements in 'l'.
        for i in range(n):
            l_copy[i] -= 1
        print(l_copy)

    return result


# False
test1 = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]
# False
test2 = [4, 2, 0, 1, 5, 0]
# True
test3 = [3, 1, 2, 3, 1, 0]
# True
test4 = [16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]
# True
test5 = [14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]
# False
test6 = [15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]
# False
test7 = [6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]
# False
test8 = [2, 2, 0]
# False
test9 = [3, 2, 1]
# True
test10 = [1, 1]
# False
test11 = [1]
# True
test12 = []

