from config import DELIMITERS
from analysis.helpers import is_number


# Split the text into tokens (words, numbers)
def tokenize(text):
    tokens = []
    current_token = ''  # Current word
    for char in text:
        if char not in DELIMITERS:
            current_token += char
        else:
            if current_token:
                process_token(current_token, tokens)
                current_token = ''

    if current_token:
        process_token(current_token, tokens)

    return tokens


# Process a single token, checking whether it is a number
def process_token(token, tokens_list):
    if is_number(token):
        try:
            num = float(token)
            tokens_list.append(num)
        except ValueError:
            tokens_list.append(token)
    else:
        tokens_list.append(token)
