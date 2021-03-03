# also known as anonymous functions in other languages

# used instead of defining a function, behave like functions, but cannot be reused and look different

def add(num1, num2):
    return num1 + num2


print(add(2, 3))

# turning this into a lambda expression

# addition = lambda num1, num2: num1 + num2
#
# print(addition(2, 3))

# does the exact same thing as the function
#   set to an object
#   then lambda and parameters/arguments
#   finally after the colon, what is happening to the arguments


# MAP()

def square_func(num):
    return num ** 2


numbers_list = [1, 2, 3, 5, 6, 7, 8, 8]

squared_numbers = map(square_func, numbers_list)
print(list(squared_numbers))

# map allows us to iterate through a list and perform a function without a for loop
#   must cast to a list 'list()' or the object cannot be accessed
#    dont need () for the function,a s no arguments are needed, map knows the iterable (numbers_list) is the argument

# inserting a lambda function

squared_numbers = map(lambda num: num ** 2, numbers_list)
print(list(squared_numbers))

# and this then does exactly the same thing as when we used the functions

# this is where lambdas are very helpful as you can write them straight into the map(), no need to define them first


# ANOTHER EXAMPLE

salary = [230, 350, 540, 430]

bonus = map(lambda num: round(num * 1.1), salary)
print(list(bonus))

# used round() as there were too many 0s after the decimal point


# look over

