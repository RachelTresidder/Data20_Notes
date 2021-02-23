# need a car that drives

# need a function for speed
# need a function for direction
# need a function for turning

# def trial():
#     pass
# this skips the function

def speed():
    mph = input("How fast would you like to go? Choose a number from 1 to 50 mph")
    return mph
# this is the up value

# print(speed())


def direction():
    choice = input("Which direction would you like to go in? Choose either UP or DOWN").lower()
    direction_counter = 0
    if choice == "up":
        direction_counter += 1
    else:
        direction_counter -= 1
    return direction_counter

# print(direction())


def turn():
    way = input("Which way would you like to turn? Choose either LEFT, RIGHT, or STRAIGHT").lower()
    turn_counter = 0
    if way == "left":
        turn_counter -= 1
    elif way == "straight":
        turn_counter = 0
    else:
        turn_counter += 1
    return turn_counter
# across value in here

# this is not working with positive and negative values


def main():
    destination = [30, 50]
    print(destination)
    coordinates = [0,0]
    while coordinates != destination:
        if coordinates == destination:
            print("You have arrived")
        else:
            print("You haven't reached your destination, keep going")
            print(f"these are your current coordinates: {coordinates}")
            coordinates[0] = int(coordinates[0] + (int(turn()) * int(speed())))
            coordinates[1] = int(coordinates[1] + (int(direction()) * int(speed())))

print(main())

# not subtracting negatives



