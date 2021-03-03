# print("hi")  # just checking my python was working
#
# new_variable = 5
# print(new_variable)
#
# # in other languages the data type would need to be specified
# # python assumes the data type for us
#
# print(type(new_variable))
# # returns the data type of the variable - here 'int'
#
# # can specify the datatype:
#
# variable2 = 5
#
# variable3 = float(variable2)
# print(type(variable2))
# print(type(variable3))
#
# # to comment out a block of text use ctrl + /
#
# # numerical operators ->  +  -  /  *  >  <  >=  <=
#
# print(5+2)
# print(5*2)
#
# a = 5
# b = 2
# print(a+b)
# print(a*b)
# # can swap numbers for variables (here integers)
#
# a1 = "5"
# b1 = "2"
# print(a1+b1)
# # because the values are now strings, it concatenated to 52, instead of printing 7
#
# # cannot concatenate a string variable and an integer/number variable
#
# print(a>b)
# # returns either true or false
#
# print(a%b)
# # returns the remainder form the division = 1
#
#
# # quotes
#
# single = 'this is a single quotes'
# double = "this is a double quotes"
#
# print(single + ' ' + double)
# # quotes work in the same way but should use both is quotes in a sentence
#
#
# # escape characters
#
# esc = 'this is \'escaped\''
# print(esc)
# # another way of putting quotes into a sentence


# # String slicing
#
# hello = "Hello World"
#
# print(hello)
#
# print(hello[6:10])
# # right of colon = inclusive
# # left of colon = exclusive -> misses the d off of world even though the '11th' letter is specified
#
# print(hello[6])
# # returns the 'seventh' value - start counting from 0
#
# hello2 = 'Hello World                  '
#
# print(hello2.strip())
# # ignores all the spaces
#
# hello3 = 'Hello World'
#
# print(hello3.count('Hello'))
# # counts the number of instances of the value's existence in the string, hence here returns 1
#
# print(hello3.upper())
# print(hello3.lower())
# # useful in ensuring all data is in the same case
#
#
# hi = 'Hello'
# name = 'jenny!'
# age = 11
#
# print(f"{hi} {name} You are {age} years old!")
# # f-strings make it easy to concatenate integers into strings and loose the + signs
#
#
#
# # boolean methods
#
# print(hi.isalpha())  # true
# print(name.isalpha())  # false - ! included
# # using .is = plenty of different checks
# # all return boolean values, ture or false, as it is checking a condition
#
# print(hi.islower())  # false, H
# print(name.islower())  # true!
# # print(age.islower())  # not possible!
#
# # '.is' is really good for checking if values have certain qualities


# x = None  # basically NULL
# y = False
#
# print(bool(x))
# print(bool(y))
# # both are false
#
# print(x == False)
# print(y == False)
# # x is equivalent to NULL, so it can't be true as it is not false
# # y is false, so the y == false returns true
#
# #  to get x to return true, use either:
# print(x == None)
# print(x is None)
# # because None is a value in its own right


# Collections

# a list is a collection of characters -> []
# a tuple is a pair of characters that cannot be edited

# shopping_list = ["cheese", "avocados", "apples"]
# #this is a list
#
# print(shopping_list)
# print(type(shopping_list))
# # returns all values, then returns the class 'list'
#
# print(shopping_list[0])
# #returns the first value = cheese
#
# print(shopping_list[-1])
# # returns the last value = apples
#
# shopping_list.append("sugar")
# print(shopping_list)
# # added sugar
#
# shopping_list[0] = "milk"
# print(shopping_list)
# # now milk is in the place of cheese
#
# print(len(shopping_list))
# # counts the individual strings within the list
# # here, returns 4
#
# print(len(shopping_list[1]))
# # returned the length of avocados = 8
#
# shopping_list.remove("avocados")
# print(shopping_list)
# # avocados is no longer in the list
#
#
# print(shopping_list[:2])
# # returns the first 2 items
#
# shopping_list = ["cheese", "avocados", "apples", "milk", "dfgr", "sdf"]
# print(shopping_list[::2])
# # # returned certain values - skipped over values with a step-size of 2

#
# shopping_tup = ("cheese", "avocados", "apples", "milk", "dfgr", "sdf")
# # this is a tuple
# print(shopping_tup)
# print(type(shopping_tup))
#
# # tuples cannot be changed (immutable)
#
# print(shopping_tup[0])
# # still returns values, same as a list, but cannot add or remove values


# Dictionaries

old_dict = {"jeff": "goldblum", "num": 1}

# use {}, you have key value pairs inside and can have more than 1 pair using a  ','
new_dict = {"my_key": "values", "num": 3,
            "key_list": ["val1", "val2", "val3"]}

# add values into a dictionary using update
# create a new dictionary and append it to the old one
old_dict.update(new_dict)
print(old_dict)

new_dict.update([("number", 1), ("hi", 4)])

print(new_dict)
# we can see everything inside the {}

print(new_dict["num"])
# returns the value associated with "num" - accessed using the key name - = 3

print(new_dict['key_list'][0])
# returns the index 0 value from the key_list paired set of values

print(new_dict.keys())
# returns all the key names within the dictionary

print(new_dict.values())
# returns all of the values

new_dict["my_key"] = "something else"
print(new_dict.keys())
# changed the key value to something else


# control flow - loops

num = 10

if num == 10:
    print("num = 10")
elif num < 10:
    print("num is less than 10")
else:
    print("num is greater than 10")

# can play with thi by changing num's value

# == means is equal to

# diff between if and elif:
#   if looks at the whole input
#   elif looks at only the part of the input that was not ture for the if statement

# use elif, if things are mutually exclusive
# use if, if not mutually exclusive
