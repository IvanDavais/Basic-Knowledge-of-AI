import Basic_Python.Function_Basic.wf_08_print_arbitray_character


def print_5times_char(char, row, col):
    """ This function can print any character for any row and any column

    :param char: character
    :param row: row
    :param col: column
    """
    i = 0

    while i < row:
        Basic_Python.Function_Basic.wf_08_print_arbitray_character.print_arbitrary_char(char, col)
        i += 1


print_5times_char("-", 8, 10)

