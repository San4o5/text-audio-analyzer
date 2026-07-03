from analysis.helpers import is_number


# Count the number of numbers among the tokens.
def count_digits(tokens):
    count = 0
    for token in tokens:
        if is_number(token):
            count += 1

    return count


# Count the number of sign changes between numbers (positive/negative/zero)
def alternation_count(tokens):
    states = []

    for token in tokens:
        if is_number(token):
            num = float(token)
            if num > 0:
                states.append('POS')
            elif num < 0:
                states.append('NEG')
            else:
                states.append('ZERO')

    if not states:
        return 0

    count = 0  # Number of sign changes
    for i in range(1, len(states)):
        # Current number's state against the previous number's state
        if states[i] != states[i - 1]:
            count += 1

    return count
