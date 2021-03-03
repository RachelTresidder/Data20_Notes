#
# Task:
# Create a simple for loop for FizzBuzz -
#  The program asks you to print “Fizz” for the multiple of 3,
# “Buzz” for the multiple of 5,
#  and “FizzBuzz” for the multiple of both
#
# Make sure to push your solution to your github account

# for i in range(100):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# turning it into a function

def fizzbuzz_function(num: int):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


print(fizzbuzz_function(29))
# return stops the code, so if going through a list should use 'print' instead
