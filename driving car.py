# need a car that drives

# need a function for speed
# need a function for direction
# need a function for turning

# def trial():
#     pass
# this skips the function

def speed():
    mph = input("How fast would you like to go? Choose a number from 1 to 5")
    return mph

# print(speed())


def direction():
    choice = input("Which direction would you like to go in? Choose either FORWARDS or BACKWARDS").lower()
    direction_counter = 0
    if choice == "forwards":
        direction_counter += 1
    else:
        direction_counter -= 1
    return direction_counter

# print(direction())


def turn():
    way = input("Which way would you like to turn? Choose either LEFT or RIGHT").lower()
    turn_counter = 0
    if way == "left":
        turn_counter = 10
    else:
        turn_counter = -10
    return turn_counter

# this is not working with positive and negative values


movement = int(speed()) * int(direction())
print(movement)

movement_turning = movement * int(turn())
print(movement_turning)

# def total_movement():
#     movement = speed() * direction()
#     return movement
# pass

# print(total_movement)
