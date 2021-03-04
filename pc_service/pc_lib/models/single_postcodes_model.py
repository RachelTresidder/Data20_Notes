class SinglePCModel:

    def __init__(self, single_postcode):
        self.status = single_pc_json['status']  # returns the status
        self.result = single_pc_json['result']  # returns the result dictionary
        self.postcode = self.result['postcode']
        self.quality = self.result['quality']
        self.eastings = self.result['eastings']
        self.northings = self.result['northings']
        self.country = self.result['country']
        self.nhs_ha = self.result['nhs_ha']
        self.admin_county = self.result['admin_county']
        self.admin_ward = self.result['admin_ward']
        self.longitude = self.result['longitude']
        self.latitude = self.result['latitude']
        self.parliamentary_constituency = self.result['parliamentary_constituency']
        self.european_electoral_region = self.result['european_electoral_region']
        self.primary_care_trust = self.result['primary_care_trust']
        self.region = self.result['region']
        self.parish = self.result['parish']
        self.lsoa = self.result['lsoa']
        self.msoa = self.result['msoa']
        self.ced = self.result['ced']
        self.ccg = self.result['ccg']
        self.nuts = self.result['nuts']
        self.codes = self.result['codes']  # returns the 'codes' dictionary
        self.codes_admin_district = self.codes['admin_district']
        self.codes_admin_county = self.codes['admin_county']
        self.codes_admin_ward = self.codes['admin_ward']
        self.codes_parish = self.codes['parish']
        self.codes_ccg = self.codes['ccg']
        self.codes_nuts = self.codes['nuts']


# passing the postcode into the () with 'single_postcode'
# we are creating attributes for all of the different keys in the 'result' dictionary, after self.result
# at the bottom, another dictionary called 'codes' is accessed

# this will represents the data
#   here we are working with classes in a different way - to access data in a dictionary using objects
#       all stored as class attributes

# this approach is very common with strongly typed languages
#      called 'service object modelling'

# we can now got to single_pc and create things
