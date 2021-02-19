# Create a script that will collect user input to store some user information and then print it back to the user.
#
# Include information about:
# - name
# - age
# - address (collect different parts separately)
# - favourite films
#
# Make sure to push your solution to your github account

name = input("Please enter your name ")
age = input("What is you age? ")
house_number= input("What is you house number? ")
street = input("What is the name of the street you live on? ")
town = input("What is your town? ")
county = input("What is your county? ")
postcode = input("What is your postcode? ")
film1 = input("What is your favourite film?")
film2 = input("What is your second favourite film?")
film3 = input("what is your third favourite film?")

print(f"\nHi {name}! \n"
      f"You are {age} years old. \n" 
      f"Your address is {house_number} {street}, {town}, {county}, {postcode} \n"
      f"Your favourite films are {film1}, {film2}, and {film3}.")