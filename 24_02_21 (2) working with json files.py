import json
# need this with everything!!!

# new_dict = {"name": "apple", "flavour": "tasty"}
#
# print(type(new_dict))
# print(new_dict)

# created a dictionary, which is a basic json file

# new_json_string = json.dumps(new_dict)
#
# print(type(new_json_string))
# print(new_json_string)

# a json here is a string as json.dumps formats a json file/dictionary into a string (need the 's' on dumps)

# json.dump needs a file to write to (no 's')

# with open("new_json_file.json", "w") as json_1st_file:
#     json.dump(new_dict, json_1st_file)

# this created a new json file and wrote the dictionary into it


# with open("new_json_file.json") as json_2nd_file:
#     fruit = json.load(json_2nd_file)
#     print(type(fruit))
#     print(fruit['name'])

# json.loads (note the 's') requires a json string

# new_fruit = "orange"
# new_flavour = "tangy"
# fruit['name'] = new_fruit
# fruit['flavour'] = new_flavour

# replaced, not added

# fruit.update({'name': 'orange'})
# fruit.update({'flavour': 'tangy'})

# still wrote over, didn't add
# print(fruit)


def rates_retrieval(file):
    with open(file) as exchange_rates:
        rates = json.load(exchange_rates)
        retrieval = rates['rates']
        print(retrieval)
        print(type(retrieval))
# retrieved the rates as a dictionary


rates_retrieval("exchange_rates.json")


def new_rates_file(file):
    with open()
    rates = rates_retrieval("exchange_rates.json")

# need to get this into a new file


def create_new_details(old_user_data_file = 'user_details.csv', new_file_name = 'new_user_details'):
    new_user_data = transform_user_details('user_details.csv')

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)



