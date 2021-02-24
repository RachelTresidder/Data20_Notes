
# creating a new variable for a file
# file = open("order.txt")

# insert file name into ""
# currently we will get a file not found error as the file does not exist

# try:
#     file = open("order.txt")
# except:
#     print("There is an error")

# now no red error message, instead our print statement is read

# try:
#     file = open("order.txt")
# except FileNotFoundError:
#     print("There is an error, the file was not found")

# now it only prints if the error is a FileNotFoundError

try:
    file = open("order.txt")
except FileNotFoundError as msg:
    print("There is an error, the file was not found")
    print(msg)

# now prints our statement and  basic error message in black text

# try:
#     file = open("order.txt")
# except FileNotFoundError as msg:
#     print("There is an error, the file was not found")
#     print(msg)
#     raise

# the raise keyword is allowing us to bring up the red error message

# try:
#     file = open("order.txt", "r")
# except FileNotFoundError as msg:
#     print("There is an error, the file was not found")
#     print(msg)

# "r" is the default, which opens the file for reading
#       "w" opens the file for writing and if the file doesnt exist, it created a new one
#       "x" is for creating a new file, but if it already exists, it just fails
#       "a" appends a file, and will create a new one if it doesnt exist
#       "t" opens a file in text mode
#       "b" opens in binary
#       "+" opens a file for reading and writing (updating)


# def open_and_print_file(file):
#     try:
#         opened_file = open(file, "r")
#         file_line_list = opened_file.readlines()    # .readlines() usually returns the lines as a list
#
#         print(file_line_list)
#
#         opened_file.close()
#         # we should always close the file after opening - otherwise you cant use the file/edit the file etc...
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#
#
# open_and_print_file("order.txt")
# printed a list that does not look good


# def open_and_print_file_better(file):
#     try:
#         opened_file = open(file, "r")
#         file_line_list = opened_file.read()
#
#         print(file_line_list)
#
#         opened_file.close()
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#
#
# open_and_print_file_better("order.txt")
# now the file shows exactly as it is


# iterating through and removing \n
# def open_and_print_file_brute_force(file):
#     try:
#         opened_file = open(file, "r")
#         file_line_list = opened_file.readlines()
#
#         for i in file_line_list:
#             i.rstrip("\n")
#             print(i)
#
#         print(file_line_list)
#
#         opened_file.close()
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)


# open_and_print_file_brute_force("order.txt")

# def open_and_print_file_better(file):
#     try:
#         opened_file = open(file, "r")
#         file_line_list = opened_file.read()
#
#         print(file_line_list)
#
#         opened_file.close()
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#     finally:
#         print("Execution Complete")
#
#
# open_and_print_file_better("order.txt")

# now we have something at the end to tell us the process/function is finished (correctly)


# def open_and_print_and_close(file):
#     try:
#         with open(file, "r") as file:
#             file_line_list = file.read()
#             print(file_line_list)
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#     finally:
#         print("Execution Complete")
#
#
# open_and_print_and_close("order.txt")

# now we don't need the .close as the with statement closes it for us


# writing to a file

# def writing_to_file(file, order_item):
#     try:
#         with open(file, "w") as file:
#             file.write(order_item + "\n")
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
# #
# #
# writing_to_file("order.txt", "burger")
# using file.write, we write what we wish to add to the file in the brackets when running the function

# this wrote over the file!!

# def appending_to_file(file, order_item):
#     try:
#         with open(file, "a") as file:
#             file.write(order_item + "\n")
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)


# appending_to_file("order.txt", "curry")
# appending_to_file("order.txt", "rice")
# appending_to_file("order.txt", "naan")
# appending_to_file("order.txt", "chips")


# now everything is back/ has been added back in,
#       and burger is at the top of the list as the original file was replaced with "Burger"


# looking at .readlines() and .read()


# def open_and_print_readlines(file):
#     try:
#         with open(file, "r") as file:
#             file_line_list = file.readlines()
#             print(file_line_list)
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#     finally:
#         print("Execution Complete")
#
#
# open_and_print_readlines("order.txt")

# so .readlines() does need the iteration and .rstrip to get it to look good and read easily


# def open_and_print_read(file):
#     try:
#         with open(file, "r") as file:
#             file_line_list = file.read()
#             print(file_line_list)
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#     finally:
#         print("Execution Complete")
#
#
# open_and_print_read("order.txt")

# but unlike .readlines(), .read() is in a perfectly readable format, same as if you viewed the txt file


# def open_as_text_and_print(file):
#     try:
#         with open(file, "rt") as file:
#             file_line_list = file.read()
#             print(file_line_list)
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#     finally:
#         print("Execution Complete")
#
#
# open_as_text_and_print("order.txt")

# reads it in text mode


# def open_binary_and_print(file):
#     try:
#         with open(file, "rb") as file:
#             file_line_list = file.read()
#             print(file_line_list)
#
#     except FileNotFoundError as msg:
#         print("There is an error, the file was not found")
#         print(msg)
#     finally:
#         print("Execution Complete")
#
#
# open_binary_and_print("order.txt")

# this one was odd! The outputs all have "\r\n <item name>" repeated until the end of the list

# internet person says:
#  on linux, there's no difference between text mode and binary mode
#       in windows, it converts \n to \r\n when not in text mode (i.e. in binary)
# so the \r\n just indicated that it is being read using binary

# write = only one object at a time to be written
# writelines = multiple arguments/ a list of things fot it to write lines for, separated by commas


# OPENING AND USING .csv files

# import csv
#
# with open('example.csv') as csv.file:
#     readCSV = csv.reader(csv.file, delimiter = ',')
#     for row in readCSV:
#         print(row)
#         print(row[0])
#         print(row[0], row[1], row[2],)

# this code is for opening a csv file and reading each row


# import csv
#
# with open('example.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     dates = []
#     colors = []
#     for row in readCSV:
#         color = row[3]
#         date = row[0]
#
#         dates.append(date)
#         colors.append(color)
#
#     print(dates)
#     print(colors)

# this code pulls out specific data from the spreadsheet and saves it to a list variable


# whatColor = input('What color do you wish to know the date of?:')
# coldex = colors.index(whatColor)
# theDate = dates[coldex]
# print('The date of',whatColor,'is:',theDate)

# having the colours printed above, this code asks for a colour, then returns the date associated with that colour
# if you ask for a colour that does not have a date/isn't in the csv, then i will throw up an error


# my code for 1 function to read, 1 function to transform, 1 function to write


# import csv
#
#
# def reading_csv(file):
#     with open(file) as csvfile:
#         readcsv = csv.reader(csvfile, delimiter=',')
#
#         for row in readcsv:
#             print(row)
#
#
# reading_csv('user_details.csv')
#
#
# def name_and_emails(file):
#     with open(file) as csvfile:
#         readCSV = csv.reader(csvfile, delimiter=',')
#
#         first_names = []
#         last_names = []
#         emails = []
#
#         for row in readCSV:
#             first_names.append(row[1])
#             last_names.append(row[2])
#             emails.append(row[3])
#
#         print(first_names)
#         print(last_names)
#         print(emails)
#
#
# name_and_emails('user_details.csv')


# paula's solutions for 1 function to read, 1 function to transform, 1 function to write:


import csv


def transform_user_details(csv_file_name):

    new_user_data = []

    with open(csv_file_name) as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')

        for row in user_details_csv:
            transformation = []
            transformation.append(row[1])
            transformation.append(row[2])
            transformation.append(row[4])
            new_user_data.append(transformation)

    return new_user_data


print(transform_user_details('user_details.csv'))

# so we now have people's details in separate lists (a list of lists)


def create_new_details(old_user_data_file = 'user_details.csv', new_file_name = 'new_user_details'):
    new_user_data = transform_user_details('user_details.csv')

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)


create_new_details()

# using the previous function, so need both to be uncommented for this bottom function to work
# a new file was created and it has the correct information in the correct format!!!

