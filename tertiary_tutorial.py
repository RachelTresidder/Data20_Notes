def check_phrase(phrase_1, phrase_2):
    phrase_1 = phrase_1.split()
    phrase_2 = phrase_2.split()

    phrase_1, phrase_2 = (phrase_1, phrase_2) if len(phrase_1) <= len(phrase_2) else (phrase_2, phrase_1)
    # tertiary structure - ensures phrase 1 is always the shorter phrase

    diff = len(phrase_2) - len(phrase_1)
    for i in range(diff):
        phrase_1.append('-')

    phrase_dict = {}

    for x in range(len(phrase_1)):
        # print(x)
        if phrase_1[x] == phrase_2[x]:
            phrase_dict.update({x: True})
            # print(True)
        else:
            phrase_dict.update({x: False})
            # print(False)

    return phrase_dict


print(check_phrase('Here is my first sentence and it is perfect', 'Here is my second sentence and it is not so great'))

# expected output:
# {0: True, 1: True, 2: True, 3: False, 4: True, 5: True, 6: True, 7: True, 8: False, 9: False, 10: False}

print(check_phrase('Here is my first sentence and it is perfect and I know why',
                   'Here is my second sentence and it is not so great'))
# phrase 1 now longer than phrase 2, still good :)
