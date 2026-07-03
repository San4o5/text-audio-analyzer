# Count the number of words among the tokens.
def count_words(tokens):
    words = []
    for token in tokens:
        if isinstance(token, str):  # Check whether the token is a string
            words.append(token)

    return len(words)


# Count the number of words of length n.
def count_words_len(tokens, n):
    count = 0
    for token in tokens:
        if isinstance(token, str) and len(token) == n:
            count += 1

    return count


# Count the number of unique words (case-insensitive)
def count_unique_words(tokens):
    normalized = []
    for token in tokens:
        if isinstance(token, str):
            normalized.append(token.lower())

    unique_words = set(normalized)

    return len(unique_words)


# Count the number of words that start with an uppercase letter.
def count_titlecase_words(tokens):
    count = 0
    for token in tokens:
        if isinstance(token, str) and token and token[0].isupper():
            count += 1

    return count
