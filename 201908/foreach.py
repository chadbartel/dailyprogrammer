"""
Weekly # 26 - Mini Challenges
../r/dailyprogrammer/comments/56mfgz/weekly_26_mini_challenges/

Description: like xargs but simpler.
Input: a file name, followed by a line of text containing a part of a shell
    command. If you want to be closer to xargs, you can directly read input from
    stdin instead of taking a filename.
Output: for every line of text in the file (or stdin), execute the shell command
    composed of the text given as argument and the line of text.

Example:
    Contents of input.txt:
        hello.txt
        world.txt
        dictionary.txt
    Usage:
        > foreach.exe input.txt echo
        hello.txt
        world.txt
        dictionary.txt
    This is equivalent to running three shell commands:
        > echo hello.txt
        > echo world.txt
        > echo dictionary.txt
    Windows example:
        $ foreach.exe input.txt cp C:\file.txt
        Will copy the file above to the files "hello.txt", "world.txt",
        "dictionary.txt"

Challenge by: /u/adrian17
"""

import os


def foreach(txt_file: str, command: str = 'echo', *args):
    """
    Like 'xargs', but simpler.
    :param txt_file: path of .txt file
    :param command: string name of shell command
    :param args: optional shell command parameters
    :return:
    """

    # Check if string passed is a text file (.txt).
    if txt_file.strip()[-4:] != '.txt':
        raise ValueError

    # Read lines of text file and apply shell command with args.
    with open(txt_file) as txt_lines:
        for txt_line in txt_lines.readlines():
            # Concatenate string parts of shell command.
            full_command = command + " ".join(args) + " " + txt_line
            os.system(full_command)

    return None
