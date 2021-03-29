import logging

# logging levels:
#   DEBUG: detailed information, typically of interest only when diagnosing problems

#   INFO: confirmation that things are working as expected

#   WARNING: an indication that something unexpected happened, or indicative of some problem in the near future
#           (e.g. 'disk space low')
#           BUT, the software is still working as expected

#   ERROR: due to a more serious problem, the software has not been able to perform some functions

#   CRITICAL: a serious error, indicating that the program itself may be unable to continue running


# logging.basicConfig(level=logging.DEBUG)
# # must use camel case, and debug MUST be in caps to differentiate from logging.debug we use further down

# # 1:
# logging.basicConfig(filename='logging_intro_test.log', level=logging.DEBUG)
# # the filename = '' creates a log file that all log data goes into

# 2:
logging.basicConfig(filename='logging_intro_test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:5(message)s')
# the filename = '' creates a log file that all log data goes into


# sample, simple functions

def add(x, y):
    """add function"""
    return x + y


def subtract(x, y):
    """subtract function"""
    return x - y


def multiply(x, y):
    """multiply function"""
    return x*y


def divide(x, y):
    """divide function"""
    return x / y


# num_1 = 10
# num_2 = 5

num_1 = 20
num_2 = 10

# add_result = add(num_1, num_2)
# print('add: {} + {} = {}'.format(num_1, num_2, add_result))
#
# subtract_result = subtract(num_1, num_2)
# print('subtract: {} + {} = {}'.format(num_1, num_2, subtract_result))
#
# multiply_result = multiply(num_1, num_2)
# print('multiply: {} + {} = {}'.format(num_1, num_2, multiply_result))
#
# divide_result = divide(num_1, num_2)
# print('divide: {} + {} = {}'.format(num_1, num_2, divide_result))


# # changing print for logging - DEBUG
# add_result = add(num_1, num_2)
# logging.debug('add: {} + {} = {}'.format(num_1, num_2, add_result))
#
# subtract_result = subtract(num_1, num_2)
# logging.debug('subtract: {} + {} = {}'.format(num_1, num_2, subtract_result))
#
# multiply_result = multiply(num_1, num_2)
# logging.debug('multiply: {} + {} = {}'.format(num_1, num_2, multiply_result))
#
# divide_result = divide(num_1, num_2)
# logging.debug('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
#
# # nothing is output to the console as the default logging level is WARNING or higher
# #   hence, debug is not a problem


# # changing DEBUG for WARNING
# add_result = add(num_1, num_2)
# logging.warning('add: {} + {} = {}'.format(num_1, num_2, add_result))
#
# subtract_result = subtract(num_1, num_2)
# logging.warning('subtract: {} + {} = {}'.format(num_1, num_2, subtract_result))
#
# multiply_result = multiply(num_1, num_2)
# logging.warning('multiply: {} + {} = {}'.format(num_1, num_2, multiply_result))
#
# divide_result = divide(num_1, num_2)
# logging.warning('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
#
# # now we get warnings output in the console:
# #   WARNING:root:add: 10 + 5 = 15
# #   WARNING:root:subtract: 10 + 5 = 5
# #   WARNING:root:multiply: 10 + 5 = 50
# #   WARNING:root:divide: 10 + 5 = 2.0
#
# # this has more info than just print:
# #   the first part is the logging level default = WARNING
# #   root is something to look at later in the tutorial
# #   and the final bit is what we passed in
#
# # BUT, this isn't really using logging correctly:
# #   we have them set as WARNING, but they are not really warnings
# #   we should really be logging them as DEBUG or INFO


# 1: go to top of file and change basic configurations


# going back to logging.debug:
add_result = add(num_1, num_2)
logging.debug('add: {} + {} = {}'.format(num_1, num_2, add_result))

subtract_result = subtract(num_1, num_2)
logging.debug('subtract: {} + {} = {}'.format(num_1, num_2, subtract_result))

multiply_result = multiply(num_1, num_2)
logging.debug('multiply: {} + {} = {}'.format(num_1, num_2, multiply_result))

divide_result = divide(num_1, num_2)
logging.debug('divide: {} + {} = {}'.format(num_1, num_2, divide_result))

# now it prints our debug statements:
#   DEBUG:root:add: 10 + 5 = 15
#   DEBUG:root:subtract: 10 + 5 = 5
#   DEBUG:root:multiply: 10 + 5 = 50
#   DEBUG:root:divide: 10 + 5 = 2.0


# creating a log file - in the config at the top
#   now the console has no output, but the output has appeared in the .log file

# changing num_1 and num_2 to 20 and 10:
#   the log file now contains info on the first run and the second run with diff numbers


# changing the format
#   https://docs.python.org/3/library/logging.html#logrecord-attributes
#   all the things that can go in the config at the top

# 2: changing things at the top again
#   now there is formatted data in the log file:
#       the date and time (, millisecond)
#       the log level
# and the message ( = message)
