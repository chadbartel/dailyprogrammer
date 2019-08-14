"""
Challenge: Given a string of alpha characters, return the morse code
equivalent for each character in sequence (without spaces).
Example:
    smorse("sos") => "...---..."
    smorse("daily") => "-...-...-..-.--"
    smorse("programmer") => ".--..-.-----..-..-----..-."
    smorse("bits") => "-.....-..."
    smorse("three") => "-.....-..."
Challenge by: u/Cosmologicon

Author: Chad Bartel
Date:   8/13/2019
"""

ALPHABET = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
MORSE_BLOB = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'


def smoosh_morse1(alpha_str: str):
    """
    Convert a text string into a concatenation of morse code.
    :param alpha_str: string of alpha characters
    :return smorse: string of dashes and dots
    """

    # Define initial variables.
    smorse = ''
    alpha_list = []
    if alpha_str.isalpha():
        alpha_list = alpha_list + list(alpha_str.upper())
    else:
        raise ValueError

    # Get dict of morse code.
    morse_dict = dict(zip(ALPHABET.split(sep=' '), MORSE_BLOB.split(sep=' ')))

    # Map each alpha character to it's corresponding morse code.
    smorse += ''.join([morse_dict[k] for k in alpha_list])

    return smorse


# "...---..."
print(smoosh_morse1("sos"))
# "-...-...-..-.--"
print(smoosh_morse1("daily"))
# ".--..-.-----..-..-----..-."
print(smoosh_morse1("programmer"))
# "-.....-..."
print(smoosh_morse1("bits"))
# "-.....-..."
print(smoosh_morse1("three"))
