# using SW1A 1AA  - buckingham palace postcode :)

# need everything in a class/classes
# extract as... (json)
# transform - get postcode, country, longitude, latitude, region
# output as something useful/somehow

import csv
import requests


class PostcodeExtract:
    def __init__(self):
        self.postcode_address = 'https://api.postcodes.io/postcodes/'
        self.postcode_complete = ''
        self.postcode = {}
        self.column_values = []
        self.needed = ['postcode', 'country', 'longitude', 'latitude', 'region']
        self.complete = []
        self.new_postcode_csv = ''

    def get_postcode_data(self, address):
        self.postcode_complete = self.postcode_address + address
        self.postcode = requests.get(self.postcode_complete)
        self.postcode = self.postcode.json()
        # print(type(self.postcode))
        # print(self.postcode)
        return self.postcode
        # gets and returns a dictionary file
        # only needs the postcode to be entered, not the full web address

    def get_columns(self):
        for key in self.postcode['result'].keys():
            if key in self.needed:
                self.column_values.append(self.postcode['result'][key])
                # print(key)
        # print(self.column_values)
        return self.column_values
        # allows me to select the correct values from within the nested dictionary called 'results'

    def final_complete(self):
        self.complete.append(self.needed)
        self.complete.append(self.column_values)
        print(self.complete)
        return self.complete
        # appends both the header(self.needed) and the values(self.column_values) into a list

    def load(self):
        with open(self.new_postcode_csv, "w", newline="") as new_postcode_file:
            csv_writer = csv.writer(new_postcode_file, delimiter=',')
            csv_writer.writerows(self.complete)
        # loads self.complete into a .csv file

    def main(self, address, new_postcode_file_name):
        self.new_postcode_csv = new_postcode_file_name
        self.get_postcode_data(address)
        self.get_columns()
        self.final_complete()
        self.load()
        # runs all the functions


instance = PostcodeExtract()
instance.main('SW1A 1AA', 'postcode_csv')