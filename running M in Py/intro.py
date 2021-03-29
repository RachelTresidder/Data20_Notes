import pymongo

client = pymongo.MongoClient()
db = client.starwars  # client['starwars']
# print(db)


# in MongoDb - use lower 'camelCase' -> findOne({})
# in pymongo use 'snake_case' -> find_one({})


luke = db.characters.find_one({"name": "Luke Skywalker"})
print(luke)
# print(type(luke))


lukes = db.characters.find({"name": "Luke Skywalker"})
# for c in lukes:
#     print(c)


# find all the droids
droids = db.characters.find({"species.name": "Droid"})
# for droid in droids:
#     print(droid)


# height of Darth Vader, only return name and height
dv = db.characters.find_one({"name": "Darth Vader"}, {"_id": 0, "name": 1, "height": 1})
# print(dv)

# another option (using dictionary syntax):
# print(dv["name"], dv["height"])


# characters with yellow eyes, only return character names
yellow = db.characters.find({"eye_color": "yellow"}, {"name": 1, "_id": 0})
# for char in yellow:
#     print(char['name'])


# male characters, only show first 3
male = db.characters.find({"gender": "male"}, {"name": 1, "_id": 0})
# male_count = 0
# for char in male:
#     if male_count != 3:
#         print(char)
#         male_count += 1
#     if male_count > 3:
#         break

# {limit:3}
# male_3 = db.characters.find({"gender": "male"}, limit=3)
# for male in male_3:
#     print(male["name"])
#
# print(male_3)


# names of humans with homeworld = Alderaan
# humans = db.characters.find({"species.name": "Human"}, {"homeworld.name": 1, "name": 1, "_id": 0})
# for char in humans:
#     if char.get('homeworld', {}).get('name') == "Alderaan":
#         print(char.get('name'))

# humans = db.characters.find({"species.name": "Human"}, {"homeworld.name": "Alderaan", "name": 1, "_id": 0})
# for char in humans:
#     print(char['name'])


# average height of female characters
heights = db.char_demo.find({"gender": "female"}, {"name": 1, "height": 1, "_id": 0})
# heights_sum = 0
# char_count = 0
#
# for char in heights:
#     if char.get('height') != "unknown":
#         # print(char)
#         heights_sum = heights_sum + int(char.get('height'))
#         char_count += 1
#
# # print(heights_sum)
# # print(char_count)
# average = heights_sum/char_count
# print(average)


# make this easier using the aggregate method in mongoDB:

avg_female_height = db.char_demo.aggregate([
    {"$match": {"gender": "female", "height": {"$ne": "unknown"}}},
    {"$group": {"_id": "$gender", "avg_height": {"$avg": "$height"}}}
])
#
# print(next(avg_female_height)['avg_height'])
# need to use char demo, as height is still a string in characters

# got the same answer as my for loop, but this is much more simple


# tallest character
tallest = db.char_demo.find({"height": {"$ne": "unknown"}}, {"name": 1, "height": 1, "_id": 0})\
    .sort("height", -1).limit(1)
#
# print(next(tallest))
#
# max_height = next(db.char_demo.aggregate([
#     {"$match": {"height": {"$ne": "unknown"}}},
#     {"$group": {"_id": None, "max_height": {"$max": "$height"}}}
# ]))['max_height']
# print(max_height)
#
# for tallboy in db.char_demo.find({"height": max_height}):
#     print(tallboy['name'], tallboy['height'])
#
# the second method is better as it allows for 2 or more characters to have a joint tallest height
#       not just looking for a single character


# can update and change records in a similar way too

