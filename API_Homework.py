# using SW1A 1AA  - buckingham palace postcode :)

# need everything in a class/classes
# extract as... (json)
# transform - get postcode, country, longitude, latitude, region
# output as something useful/somehow

import json
import csv
import requests


class PostcodeExtract:
    def __init__(self):
        self.postcode = {}
        self.json_column_values = []
        self.needed = ['postcode', 'country', 'longitude', 'latitude', 'region']
        self.complete = []
        self.new_postcode_csv = ''

    def get_postcode_data(self, address):
        self.postcode = requests.get(address)
        self.postcode = self.postcode.json()
        return self.postcode
    # this def is working and returning a json file

    def get_columns(self):
        for key in self.postcode['result'].keys():
            if key in self.needed:
                self.json_column_values.append(self.postcode['result'][key])
        print(self.json_column_values)
        return self.json_column_values

    def json_complete(self):
        self.complete.append(self.needed)
        self.complete.append(self.json_column_values)
        print(self.complete)
        return self.complete

    def load(self):
        with open(self.new_postcode_csv, "w", newline="") as new_postcode_file:
            csv_writer = csv.writer(new_postcode_file, delimiter=',')
            csv_writer.writerows(self.complete)

    def main(self, address, new_postcode_file_name):
        self.new_postcode_csv = new_postcode_file_name
        self.get_postcode_data(address)
        self.get_columns()
        self.json_complete()
        self.load()


instance = PostcodeExtract()
instance.main('https://api.postcodes.io/postcodes/SW1A 1AA', 'postcode_csv')