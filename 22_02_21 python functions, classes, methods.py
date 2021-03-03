# while loops

# while loops do something whilst something is true

x = 0

# while x < 10:
#     print(x)
#     x = x + 1

# it prints 1-9 because when it reaches 10 the loop ends
# must have a way to end the condition or else you will create an infinite condition

# can use 'break' to exit the loop immediately

# can use 'continue' to make loop with multiple statements continue with a section of the loop
#   it will cause the loop to not complete anything written below 'continue'
#       and keep going over a certain part of the loop
# CONTINUE NEEDS AN EXIT CLAUSE!!!!


# while x < 10:
#     print(x)
#     if x == 4:
#         break
#     x += 1

# this loop stopped when x was = to 4 (printed 0 to 4, but not 5)
# anything written below 'break' within the loop will not run once 'break' is activated

# we can verify user input using a while loop


# FUNCTIONS

# need to be very clear with function name so you know what it does
# also arguments should be as easy to understand as possible


# we should use 'return' in functions, not 'print'

# def add_numbers(number1 = 5, number2 = 2):
#     return number1 + number2

# in the arguments we can add default values:
#   eg. here number1 defaults to 5 and number 2 defaults to 2
#       it is also giving us type hints when we hover over the ()
#           therefore, gives a warning if wrong data type is given as input (python does this for us)
# can also put data type where default value is, to specify, using a colon instead of =
#   e.g. number1: int
#       we can specify type and give a default
# we can expect an output data type using ' -> <data type>' after the argument ()

# print(add_numbers())
# without any input, prints 5+2 = 7

# print(add_numbers("hello", "hi"))
# brings up a warning
#   but despite the warning it concatenates them because it's using +

# def add_numbers_multi(*multiargs):
#     print(multiargs)
#     print(type(multiargs))
#     for arg in multiargs:
#         print(arg)

# this will accept everything:
#   any amount of values
#   any type of values

# add_numbers_multi(3, "dfjgh", ["hello", 3])

# so this function prints everything that was input
#   it tells us that this is a tuple
#       and then iterates through the tuple (tuple = immutable list)

# single * defines the argument
#   two * (**...) is for defining a keyword argument (??? not certain of this)- object oriented python


# CLASSES

# to create a class, write "class <class name>
# class Dog:
#     animal_kind = 'canine'
#
#     def bark(self):
#         return 'woof'

# variables inside a class are called class variables and are not a good idea
# using a def in a class it passes "self into the brackets
#   self = a parameter that is a reference to the current instance of the class

# use camel-case when defining class names:
#   e.g. BestDog()

# bark()

# cannot use this method outside of the class
#   it 'belongs' to the class


# setting class variables:

# class Dog:
#     animal_kind = 'canine'
#
#     def bark(self):
#         print(self.animal_kind)
#         return 'woof'
#
#
# print(Dog.animal_kind)
# print(Dog.bark())

# inside the class, use "self." to view everything that is going on within the class
# if 'self' is removed from inside the bark brackets,
#       it says the method must have 'self' as its parameter

# trying to use Dog.bark() outside the class will not work
#       methods are only available to class objects - we do not yet have an object


# creating class objects
# class Dog:
#     animal_kind = 'canine'
#
#     def bark(self):
#         print(self.animal_kind)
#         return 'woof'
#
# husky = Dog()

# we have created an object and instantiated a class

# print(type(husky))
# returns that it is a class '__main__Dog'

# print(husky.bark())
# now returns 'woof' and 'canine'

# print(husky.animal_kind)
# returns canine

# Lacy = Dog()

# added another dog

# changing the animal kind
# husky.animal_kind = "Big Dog"

# print(husky.animal_kind)
# print(Lacy.animal_kind)
# husky is now a 'Big Dog' but Lacy is still 'canine'

# WE CAN HAVE MULTIPLE OBJECTS THAT CAN ADAPT AND CHANGE within a class

# Dog.animal_kind = "Dolphin"
# print(husky.animal_kind)
# print(Lacy.animal_kind)

# only Lacy changes to a dolphin, husky remains as a 'Big Dog'
#       husky has already been defined, but Lacy reverts to the default, which was changed


# init construct method
# class Dog:
#     animal_kind = 'canine'
#
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self.bark()
#
#     def bark(self):
#         print('woof')
#         return 'woof'

# initialises the class
#   sets specific variables
#       need self.<name> to specify the values


# now we need a name and breed for the dog
# Lacy = Dog("Lacy", "jack russel")
# Husky = Dog("Husky", "husky")
# because the bark def is in the init, it causes bark to happen too

# print(Lacy.breed)
# accessing the breed

# print(Lacy.name)
# accessing the name

# class Dog:
#     animal_kind = 'canine'
#
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self.bark()
#
#     def bark(self):
#         print('woof')
#         return 'woof'

# ACCESSIBILITY OF CLASS STUFF

# methods should be made either public or private
#       public = easy to change, accessible by anything
#       private = accessible only by the class itself
# right now, all the above is available (public)
# this forms part of the encapsulation principles


# using _ you can hide things in python
# class Dog:
#     animal_kind = 'canine'
#
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self.__bark()
#
#     def __bark(self):
#         print('woof')
#         return 'woof'

# the two __ make 'bark' only available to the class
#   'Dog.' will no longer give 'bark' as an option

# good for stopping people from accessing things directly that they should not be able to change


# DIFFERENT EXAMPLE

# calling and setting variables

class MethodExamples:

    def __init__(self):
        self._this_can_be_accessed = "I can access easily"

    def get_this_can_be(self):
        return(self._this_can_be_accessed)  # this can be accessed by the method but not by using
        # 'MethodExamples.' - it doesnt appear as an option

    def set_this_can_be(self, value_to_be_set):
        self._this_can_be_accessed = value_to_be_set

x = MethodExamples
# 'x.'  #  shows/accesses everything outside the class despite the _

# need __ to make it invisible/un-accessible
# e.g.
# class MethodExamples2:
#
#     def __init__(self):
#         self._this_can_be_accessed = "I can access easily"
#
#     def __get_this_can_be(self):
#         return(self._this_can_be_accessed)  # this can be accessed by the method but not by using
#         # 'MethodExamples.' - it doesnt appear as an option
#
#     def set_this_can_be(self, value_to_be_set):
#         self._this_can_be_accessed = value_to_be_set
#
# x = MethodExamples2

# now 'get_this_can_be' will not be visible using 'x.'


# INHERITANCE

# creating a class for the parent
class Animal:
    def __init__(self):
        self.alive = True
        self.breathe()

    def breathe(self):
        print("one breath in, one breath out")


# this is inheritance from the parent:
class LandMammal(Animal):

    def __init__(self, legs):
        super().__init__()
        self.limbs = legs

    def run(self):
        print("I can run!")


Horse = Animal()
Mammoth = LandMammal(4)

# mammoth has everything a horse has,  as well as having 4 legs and can run

print(Horse.breathe)

Horse.alive = False
# technically killed the horse!!!

print(Mammoth.breathe())

# that is basically inheritance


# WITHIN DATA ENGINEERING

# classes are useful for:
#   ETL - you can have a class for extraction, a class for transformation, and a class for loading
# good to use inheritance because inheritance allows data to be
