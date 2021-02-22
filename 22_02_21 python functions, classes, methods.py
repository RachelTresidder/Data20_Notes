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

def add_numbers(number1 = 5, number2 = 2):
    return number1 + number2

# in the arguments we can add default values:
#   eg. here number1 defaults to 5 and number 2 defaults to 2
#       it is also giving us type hints when we hover over the ()
#           therefore, gives a warning if wrong data type is given as input (python does this for us)
# can also put data type where default value is, to specify, using a colon instead of =
#   e.g. number1: int
#       we can specify type and give a default
# we can expect an output data type using ' -> <data type>' after the argument ()

print(add_numbers())
# without any input, prints 5+2 = 7

print(add_numbers("hello", "hi"))
# brings up a warning
#   but despite the warning it concatenates them because it's using +

def add_numbers_multi(*multiargs):
    print(multiargs)
    print(type(multiargs))
    for arg in multiargs:
        print(arg)

# this will accept everything:
#   any amount of values
#   any type of values

add_numbers_multi(3, "dfjgh", ["hello", 3])

# so this function prints everything that was input
#   it tells us that this is a tuple
#       and then iterates through the tuple (tuple = immutable list)

# single * defines the argument
#   two * (**...) is for defining a keyword argument (??? not certain of this)- object oriented python

