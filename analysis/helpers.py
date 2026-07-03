from config import DELIMITERS


# Check whether a character is a delimiter
def is_delimiter(char):
    return char in DELIMITERS


# Check whether a token is a number
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
