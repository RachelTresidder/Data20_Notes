# Determine if a word or phrase is an isogram using a for loop and if statements.
#
# An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter,
# however spaces and hyphens are allowed to appear multiple times.
#
# Examples of isograms:
# lumberjacks
# background
# downstream
# six-year-old
#
# The word isograms, however, is not an isogram, because the s repeats.
#
# Make sure you push your solution to your github account.

# def is_isogram(word):
#     word = word.lower()
#     total = 0
#     for i in word:
#         total = total + 1
#     if total == len(word):
#         if word.count(i) > 1:
#             return False
#     return True
#
# print(is_isogram("lumberjack"))
#
# print(is_isogram("six-year-old"))
#
# print(is_isogram("Hello"))
# this still isn't iterating for the return false clause

# this wont ignore punctuation/spaces


#more simple, working method

def iso(x):
    temp = x.lower()
    for i in temp:
        if i.isalpha() and temp.count(i) > 1:
            return False
    return True

print(iso("lumberjack"))

print(iso("six-year-old"))

print(iso("Hello"))


# code from the internet:

# def check_isogram(str1):
#     return len(str1) == len(set(str1.lower()))
#
# print(check_isogram("w3resource"))
# print(check_isogram("w3r"))
# print(check_isogram("Python"))
# print(check_isogram("Java"))
# # testing
# print(check_isogram(input("Enter a word ")))
