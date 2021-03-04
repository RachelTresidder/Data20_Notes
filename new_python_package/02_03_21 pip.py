# pip ==  pip installs packages

# different to import ...

# pip installs packages that you might with to use
#   e.g. import requests

# import requests

# can hover over, click the red light bulb, and select install packages

# now I have imported, it's now in white, not red underlined

# can also create a package using new -> python package
# init.py initialises the package
#   folder called python_package

# never call files the same thing as package names

# new directory is different to python package,
#   but, can create a file called __init__.py in a directory
#       nothing goes into __init__.py
#           also, the directory folder has changed to that of a package folder!

# setup.py:
#   a file that will describe the details of ownership, distribution, etc..
#   main thing we need is to import setup tools
#       go and see set up for necessary code

# fizzbuzz.py  = the code
#   we can import functions or classes


import requests
# go to postcodes.io

# 'look up a postcode'
# -> get - request button, after adding in a postcode
# gives the info about the postcode = json format

# APIs will be either json or xml, but more foten json


# (back in pycharm)
post_codes_req = requests.get('https://api.postcodes.io/postcodes/se120nb')
# use the web address


print(post_codes_req)
# gives the status code, not the data

print(post_codes_req.headers)
# gives the key value pairs

print(post_codes_req.content)
print(type(post_codes_req.content))
# bytes array format

print(post_codes_req.json())
print(type(post_codes_req.json()))
# dictionary format









