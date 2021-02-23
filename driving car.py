# need a car that drives

# need a function for speed
# need a function for direction
# need a function for turning

# def trial():
#     pass
# this skips the function


import random
# from math import *


def random_destination():
    random_coordinates = [0, 0]
    random_coordinates[0] = random.randint(-50, 50)
    random_coordinates[1] = random.randint(-50, 50)
    return random_coordinates


# print(random_destination())


def distance():
    meters = input("How fast would you like to go? Choose a number from 1 to 20 meters ")
    return meters
# this is the up value

# print(speed())


def direction():
    choice = input("Which direction would you like to go in? Choose either UP or DOWN ").lower()
    direction_counter = 0
    if choice == "up":
        direction_counter += 1
    else:
        direction_counter -= 1
    return direction_counter

# print(direction())


def turn():
    way = input("Which way would you like to turn? Choose either LEFT, RIGHT, or STRAIGHT ").lower()
    turn_counter = 0
    if way == "left":
        turn_counter -= 1
    elif way == "straight":
        turn_counter = 0
    else:
        turn_counter += 1
    return turn_counter


def final_destination():
    destination = random_destination()
    print(destination)
    coordinates = [0, 0]
    while coordinates != destination:
            print("You haven't reached your destination, keep going")
            print(f"these are your current coordinates: {coordinates} \n")
            coordinates[0] = int(coordinates[0] + int((int(turn()) * int(distance()))))
            coordinates[1] = int(coordinates[1] + int((int(direction()) * int(distance()))))
    if coordinates == destination:
        print("You have arrived")


print(final_destination())


# def temperature():
#     temp_dest = (int(destination[0]) + int(destination[1])) ^ 2
#     temp_coord = (int(coordinates[0]) + int(coordinates[1])) ^ 2
#     difference = sqrt(int(temp_dest + temp_coord))
#     if difference < 20:
#         return("Hot!")
#     elif difference > 20 and difference < 50:
#         return("warm")
#     else:
#         return("cold..... :( ")

# need a while loop here too

# ((x - x2) ^2) + ((y - y2)) ^2 = sqrt(x3 + y3)
