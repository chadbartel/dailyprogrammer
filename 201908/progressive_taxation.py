"""
Challenge: Given the tax bracket below, find the amount of tax owed for any
integer less than 100,000,000.
Example:
    income cap      marginal tax rate
        10,000          0.00 (0%)
        30,000          0.10 (10%)
       100,000          0.25 (25%)
            --          0.40 (40%)
Challenge by: u/Cosmologicon

Author: Chad Bartel
Date:   8/11/2019
"""

from math import floor


def progressive_taxation(income: int):
    """
    Calculate the amount of taxes owed for a given income amount.

    :param income: taxable money received for work/investments
    :return tax_owed: money owed to the government
    """

    # Calculate tax amount for each bracket.
    if income <= 10000:
        tax_owed = 0
    elif 10000 < income <= 30000:
        tax_owed = 0 + (income-10000)*0.1
    elif 30000 < income <= 100000:
        tax_owed = 0 + 20000*0.1 + (income-30000)*0.25
    else:
        tax_owed = 0 + 20000*0.1 + 70000*0.25 + (income-100000)*0.4

    return floor(tax_owed)


# 0
print(progressive_taxation(0))
# 0
print(progressive_taxation(10000))
# 0
print(progressive_taxation(10009))
# 1
print(progressive_taxation(10010))
# 200
print(progressive_taxation(12000))
# 8697
print(progressive_taxation(56789))
# 473326
print(progressive_taxation(1234567))
