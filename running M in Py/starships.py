import pymongo
import requests
import logging

client = pymongo.MongoClient()
db = client.starwars  # client['starwars']
# print(db)


# TASK:

# in python write something that will pull data on starships from a starwars api
#   swapi.dev - https://swapi.dev -> search starships

# use requests package to pull data
# use pymongo to get data about starships

# query starship api for a ship
#   then query all urls in pilots field to get who pilots that ship
#       then replace urls for the pilots with the character object Ids from characters

# at least use functions


# # CODE:
#
#
# def create_database(db_name):
#     db.create_collection(db_name)
#     # creating a new collection
#
#
# ships_list = []
# url = ''
#
# # test = ships = requests.get("https://swapi.dev/api/starships/?page=5").json()
# # print(test)
# # max of 4 pages to look at
#
# # should put this into a function to get number of pages
#
#
# def get_ships():
#     page = 1
#     while page < 5:
#         if page < 5:
#             url = "https://swapi.dev/api/starships/?page="
#             ships = requests.get(url + str(page)).json()
#             # print(page)
#             # print(ships)
#             # print(ships['results'])
#             ships_list.append(ships['results'])
#             page += 1
#     return ships_list
#
#
# def upload_ships():
#     ships_dict = {}
#     ship_count = 0
#     for page in ships_list:
#         # print(page)
#         for ship in page:
#             # print(ship)
#             db.starships_api.insert_one(ship)
#     # print(ships_dict)
#     # this uploaded everything to the database :)
#
#
# def change_pilot_urls():
#     # now querying and finding the values of pilots in the database, looking them up, then changing them for the ids
#     star_ships = db.starships_api.find({})
#     # print(star_ships)
#     # # found all the ships
#
#     pilot_id = ''
#
#     for ship in star_ships:
#         # print(ship)
#         pilots = ship.get('pilots')
#         if pilots != []:
#             print(pilots)
#             pilots_list = []
#             example_list = []
#             for pilot in pilots:
#                 # print(pilot)
#                 pilot_details = requests.get(pilot).json()
#                 pilot_name = pilot_details.get('name')
#                 # print(pilot_details)
#                 # print(pilot_name)
#                 match = db.char_demo.find({'name': pilot_name}, {'_id': 1})
#                 # print(match)
#                 for info in match:
#                     # print(info)
#                     # print(info['_id'])
#                     pilot_id = str('ObjectId' + "('" + str(info['_id']) + "')")
#                     # print(pilot_id)
#                     pilots_list.append(pilot_id)
#                 # print(pilots_list)
#
#             updated = db.starships_api.update_one({'pilots': pilots}, {'$set': {'pilots': pilots_list}})
#
#     print(updated)
#     print(type(updated))
#     print("acknowledged:", updated.acknowledged)
#
#     # integer of the number of docs modified
#     print("number of docs updated:", updated.modified_count)
#
#     # dict object with more info on API call
#     print("raw_result:", updated.raw_result)
#     #
#     for i in db.starships_api.find({}):
#         print(i)
#     # can use this to check the db now
#
#     return updated


# RUNNING THE FUNCTIONS:

# create_database('starships_api')
# #   only need to run this function once
#
#
# get_ships()
#
#
# upload_ships()
# #   this uploaded everything to the database :) - only needed to run this once
#
#
# change_pilot_urls()
# #   can only run this once because then there will be no urls to update!


# LOGGING PRACTICE (with a new collection and cleaner code)

logging.basicConfig(filename='starships_api_2.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def create_database2(db_name):
    db.create_collection(db_name)
    # creating a new collection


ships_list = []

# test = ships = requests.get("https://swapi.dev/api/starships/?page=5").json()
# print(test)
# max of 4 pages to look at

# should put this into a function to get number of pages


def get_ships2():
    page = 1
    while page < 5:
        if page < 5:
            url = "https://swapi.dev/api/starships/?page="
            ships = requests.get(url + str(page)).json()
            logging.info(f"this is a page from the api: {page}")
            logging.info(f"the ships from the page: {ships['results']}")
            ships_list.append(ships['results'])
            page += 1
    return ships_list


def upload_ships2():
    for page in ships_list:
        for ship in page:
            db.starships_api_2.insert_one(ship)
    # this uploaded everything to the database :)


def change_pilot_urls2():
    # now querying and finding the values of pilots in the database, looking them up, then changing them for the ids
    star_ships = db.starships_api_2.find({})
    # # found all the ships

    for ship in star_ships:
        pilots = ship.get('pilots')
        if pilots != []:
            logging.info(f"the list of pilots for a specific ship: {pilots}")
            pilots_list = []
            for pilot in pilots:
                pilot_details = requests.get(pilot).json()
                pilot_name = pilot_details.get('name')
                logging.info(f"name of a pilot from the ship: {pilot_name}")
                match = db.char_demo.find({'name': pilot_name}, {'_id': 1})
                # match = db.char_demo.find({'name': pilot_name}, {'_id': 1})[0]['_id']
                #   allows access to the first item within the cursory object (so no need for the 'for loop')
                for info in match:
                    logging.info(f"the pilot object id: {info['_id']}")
                    pilot_id = str('ObjectId' + "('" + str(info['_id']) + "')")
                    pilots_list.append(pilot_id)
                logging.info(f"the list of pilot ids for the specific ship: {pilots_list}")

            updated = db.starships_api_2.update_one({'pilots': pilots}, {'$set': {'pilots': pilots_list}})

    logging.info(f"if the update worked: {updated.acknowledged}")

    # integer of the number of docs modified
    logging.info(f"number of docs updated: {updated.modified_count}")

    # dict object with more info on API call
    logging.info(f"raw_result: {updated.raw_result}")
    #
    for i in db.starships_api_2.find({}):
        print(i)
    # can use this to check the db now

    # return updated


create_database2('starships_api_2')

get_ships2()

upload_ships2()
#   this uploaded everything to the database :) - only needed to run this once

change_pilot_urls2()
#   can only run this once because then there will be no urls to update!
