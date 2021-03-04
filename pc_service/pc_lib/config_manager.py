# place for exposing the stuff in config, and using it

import configparser

# configparser requires .ini file, its a python builtin method

_config = configparser.ConfigParser()
_config.read('pc_lib/config.ini')

# instantiating a configparser and setting it to a variable

# now _config has methods available to us

_config.read('/pc_lib/config_manager.py')

# . read allows us to read the file in preparation for later use
#   need to state the package path inside ()
# only need this if config manager is in a different place to the main file


def base_url():
    return _config['DEFAULT']['base_url']


# base_url = 'https://api.postcodes.io/'

# using the base_url in a function
# creating a getter
# returning https://api.postcodes.io/

# finished config stuff
