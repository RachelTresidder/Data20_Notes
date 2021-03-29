
# Define a function that takes two string arguments,
#   and returns a list containing all the mismatched words between the two given input strings

# The function should return a list of words that are not common across the two input strings

# e.g. following two strings as inputs:
#       'This is the very first string to test'
#       'This is the second string I want to test'

# Expected output:
#       ['very', 'first', 'second', 'I', 'want']


def not_match(phrase1: str, phrase2: str):

    phrase1 = phrase1.split()
    phrase2 = phrase2.split()

    short, long = (phrase1, phrase2) if phrase1 <= phrase2 else (phrase2, phrase1)

    words_list = []

    for word in range(len(long)):
        if long[word] not in short:
            words_list.append(long[word])

    for word in range(len(long)):
        if short[word] not in long:
            words_list.append(short[word])

    return words_list


print(not_match('This is the very first string to test', 'This is the second string I want to test'))
