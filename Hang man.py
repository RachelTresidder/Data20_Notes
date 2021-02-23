# choose a word from the list

# create an object from that word that shows the number of letters as spaces

# get input of a letter

# swap the correct letters into the spaces when guessed

# specify and print a number of lives

# set up code to run all of this together
# remove a live if guess is incorrect


# getting the word

from hangman_words import word_list
import random

# word = random.choice(word_list)
# word = word.lower()
# print(word)
# word collection is working


# setting a value for word length

# length_of_word = len(word)
# print(length_of_word)
# this returns the length of word


# creating a set of spaces equal to the length of the word
# spaces = ''
# count = 0
# while count != length_of_word:
#     count += 1
#     single_space = "_"
#     spaces = spaces + single_space
#
# spaces_list = []
# count_list = 0
# while count_list != length_of_word:
#     count_list += 1
#     single_space_list = "_"
#     spaces_list.append(single_space_list)
#
# spaces_count = len(word) * '_'
#
# print(spaces)
# print(spaces_list)  # I think using the list is the best option here
# print(spaces_count) # same as spaces but simpler
# now I have the number of letters and an equal number of _ in a row


# def get_letter(letter):
#     letter = letter.lower()
#     return(letter)
#
# print(get_letter(input("Please enter a letter ")))

# successfully get input of letter set as a function
# not sure i actually need this separate, might need to incorporate


# building the whole game
word = random.choice(word_list)
word = word.lower()
# print(word)

length_of_word = len(word)
# print(length_of_word)

spaces_list = []
count_list = 0
while count_list != length_of_word:
    count_list += 1
    single_space_list = "_"
    spaces_list.append(single_space_list)

print(''.join(spaces_list))

flag = False
lives = 10
guessed_letters = []
guess = ''
guessed_words = []
while lives != 0:
    attempt = input("Please enter a letter")
    attempt = attempt.lower()
    letter = str(attempt)
    if letter in word and letter not in guessed_letters:
        print("Correct")
        guessed_letters.append(letter)
        for i in range(0, length_of_word):
            if word[i] == letter:
                spaces_list[i] = letter
        if ''.join(spaces_list) == word:
            flag = True
            break
        print(''.join(spaces_list))
        print(f"you have {lives} lives left")
        print(f"You have tried these letters so far :{guessed_letters}")
        if input("Can you guess the word yet? Y/N").lower() == "y":
            print(f"your previous guessed words are {guessed_words}")
            guess = input("Write your guess").lower()
            guessed_words.append(guess)
            if guess == word:
                print(f"You win! The word was {word}")
                break
            else:
                print("Incorrect, you loose another life")
                lives -= 1
                print(f"you have {lives} lives left")
    elif letter in guessed_letters:
        print(f"You have already tried {letter}")
    else:
        if letter not in word and len(letter) == 1 and attempt in 'abcdefghijklmnopqrstuvwxyz':
            print("Incorrect")
            guessed_letters.append(letter)
            lives -= 1
            print(f"you have {lives} lives left")
            print(f"You have tried these letters so far :{guessed_letters}")
        else:
            print("You did not enter a letter")
if lives == 0:
    print(f"You have {lives} lives remaining, you lose! \n"
          f"The word was {word}")
if flag:
    print(f"You win! The word was {word}")

# lives count is rolling down
# can return the old letters that have been guessed
# tells you if you have already guessed a letter and doesnt mark off another life
# can also filter out anything other than a relevant character (letter)
# has an exit of the loop as soon as lives reach 0, saying you lose

# all running :)
