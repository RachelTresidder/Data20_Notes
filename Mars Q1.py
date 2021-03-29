
# Define a function that takes two sentences as arguments,
#   and returns a dictionary containing information about which words match across the two

# The "matching" should be done based on the position of the word within the sentence.

# e.g. given the following two strings as inputs:
#       'Here is my first sentence and it is perfect'
#       'Here is my second sentence and it is not so great'

# Expected output:
#       {0: True, 1: True, 2: True, 3: False, 4: True, 5: True, 6: True, 7: True, 8: False, 9: False, 10: False}


def match_words(phrase1: str, phrase2: str):

    phrase1, phrase2 = (phrase1, phrase2) if len(phrase1) <= len(phrase2) else (phrase2, phrase1)

    phrase1 = phrase1.split()
    phrase2 = phrase2.split()

    diff = len(phrase2) - len(phrase1)
    for num in range(diff):
        phrase1.append('-')

    word_dict = {}

    for word in range(len(phrase1)):
        if phrase1[word] == phrase2[word]:
            word_dict.update({word: True})
        if phrase1[word] != phrase2[word]:
            word_dict.update({word: False})

    return word_dict


print(match_words('Here is my first sentence and it is perfect', 'Here is my second sentence and it is not so great'))
print(match_words('Here is my second sentence and it is not so great', 'Here is my first sentence and it is perfect'))
