from .config_manager import *

from .models.single_postcodes_model import SinglePCModel

import requests

# importing everything from config
# then importing the class
# then the requests package


class SinglePC():

    def __init__(self, single_post_code):
        self.url = base_url() + f"postcodes/{single_post_code}"  # allows for only the postcode to be entered
        self.request = requests.get(self.url)  # requests.get()retrieves the data contained within something, eg the url
        self.header_details = self.request.headers  # or requests.get(self.url).headers - gets the headers of the site
        self.response_json = self.request.json()  # holds everything from the url

    def response_data(self):
        return SinglePCModel(self.response_json)
    # passing in the self.response_json from above into the class in single_postcodes_model
    # creating the object model for our data self.response_json


# doing this in another file - postcodes_service
# new = SinglePC('SW1A 1AA')
# print(new.response_json)
