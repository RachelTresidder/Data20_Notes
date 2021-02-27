class Hangman:

    def __init__(self):
        self.random_word = ''
        self.length_of_word = ''
        self.underscores = []
        self.guessed_letters = []
        self.guess = ''
        self.guessed_words = []
        self.guess_word = ''

    lives = 10
    flag = False
    spaces_list = []
    count_list = 0
    single_space = '_'
    lose_a_life = 'Incorrect. You lose a life'
    win = 'You Win!'
    lose = 'You Lose...'

    def choose_word(self):
        from hangman_words import word_list
        import random

        word = random.choice(word_list)
        word = word.lower()
        self.random_word = word
        return self.random_word

    def word_length(self):
        self.length_of_word = len(self.random_word)
        return self.length_of_word

    def letter_underscores(self):
        while self.count_list != self.length_of_word:
            self.count_list += 1
            self.underscores.append(self.single_space)
        return self.underscores

    def guess_a_letter(self):
        self.guess = input("Please enter a letter: ")
        self.guess = self.guess.lower()
        self.guess = str(self.guess)
        return self.guess

    def guess_letter_correct(self):
        print("\nCorrect!")
        self.guessed_letters.append(self.guess)
        for i in range(0, len(self.random_word)):
            if self.random_word[i] == self.guess:
                self.underscores[i] = self.guess
        print(''.join(self.underscores))
        print(f"\nYou have {self.lives} lives left")
        return f"You have tried these letters so far :{self.guessed_letters}"

    def guess_letter_incorrect(self):
        print("\nIncorrect")
        self.guessed_letters.append(self.guess)
        self.lives -= 1
        print(''.join(self.underscores))
        print(f"\nYou have {self.lives} lives left")
        return f"You have tried these letters so far :{self.guessed_letters}"

    def check_guess(self):
        if ''.join(self.underscores) == self.random_word:
            self.flag = True
            return self.win
        elif self.guess in self.random_word and self.guess not in self.guessed_letters:
            return self.guess_letter_correct()
        elif self.guess in self.guessed_letters:
            return f"\nYou have already tried {self.guess}"
        elif self.guess not in self.random_word and len(self.guess) == 1 and self.guess in 'abcdefghijklmnopqrstuvwxyz':
            return self.guess_letter_incorrect()
        else:
            print("\nYou did not enter a letter")
            return ''.join(self.underscores)

    def guess_a_word(self):
        print(f"\nYour previous guessed words are {self.guessed_words}")
        self.guess_word = input("Write your guess: ").lower()
        self.guessed_words.append(self.guess_word)
        if self.guess_word == self.random_word:
            print(self.win)
            return f"\nThe word was {self.random_word}"
        else:
            self.lives -= 1
            print(self.lose_a_life)
            return f"\nYou have {self.lives} lives left"

    def guessing_words(self):
        yes_no = input("\nCan you guess the word yet? Y/N: ").lower()
        if yes_no == 'y':
            return self.guess_a_word()
        elif self.lives == 0:
            print(f"\nYou have {self.lives} lives remaining, you lose!"
                  f"\nThe word was {self.random_word}")
        else:
            return "\nThat's okay, keep guessing letters\n"

    def game(self):
        h = Hangman()
        h.choose_word()
        h.word_length()
        print(h.letter_underscores())
        while h.lives != 0:
            print(h.guess_a_letter())
            print(h.check_guess())
            print(h.guessing_words())


Hangman.game('hangman_words.py')


# choose a word from the list

# create an object from that word that shows the number of letters as spaces

# get input of a letter

# swap the correct letters into the spaces when guessed

# specify and print a number of lives

# set up code to run all of this together
# remove a live if guess is incorrect


#          getting the word

# from hangman_words import word_list
# import random

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


#                building the whole game
# word = random.choice(word_list)
# word = word.lower()
# # print(word)
#
# length_of_word = len(word)
# # print(length_of_word)
#
# spaces_list = []
# count_list = 0
# while count_list != length_of_word:
#     count_list += 1
#     single_space_list = "_"
#     spaces_list.append(single_space_list)
#
# print(''.join(spaces_list))
#
# flag = False
# lives = 10
# guessed_letters = []
# guess = ''
# guessed_words = []
# while lives != 0:
#     attempt = input("Please enter a letter")
#     attempt = attempt.lower()
#     letter = str(attempt)
#     if letter in word and letter not in guessed_letters:
#         print("Correct")
#         guessed_letters.append(letter)
#         for i in range(0, length_of_word):
#             if word[i] == letter:
#                 spaces_list[i] = letter
#         if ''.join(spaces_list) == word:
#             flag = True
#             break
#         print(''.join(spaces_list))
#         print(f"you have {lives} lives left")
#         print(f"You have tried these letters so far :{guessed_letters}")

#         if input("Can you guess the word yet? Y/N").lower() == "y":
#             print(f"your previous guessed words are {guessed_words}")
#             guess = input("Write your guess").lower()
#             guessed_words.append(guess)
#             if guess == word:
#                 print(f"You win! The word was {word}")
#                 break
#             else:
#                 print("Incorrect, you loose another life")
#                 lives -= 1
#                 print(f"you have {lives} lives left")

#     elif letter in guessed_letters:
#         print(f"You have already tried {letter}")

#     else:
#         if letter not in word and len(letter) == 1 and attempt in 'abcdefghijklmnopqrstuvwxyz':
#             print("Incorrect")
#             guessed_letters.append(letter)
#             lives -= 1
#             print(f"you have {lives} lives left")
#             print(f"You have tried these letters so far :{guessed_letters}")
#         else:
#             print("You did not enter a letter")
# if lives == 0:
#     print(f"You have {lives} lives remaining, you lose! \n"
#           f"The word was {word}")
# if flag:
#     print(f"You win! The word was {word}")

# lives count is rolling down
# can return the old letters that have been guessed
# tells you if you have already guessed a letter and doesnt mark off another life
# can also filter out anything other than a relevant character (letter)
# has an exit of the loop as soon as lives reach 0, saying you lose

# all running :)
