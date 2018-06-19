import configparser

FILE = "config.ini"

config = configparser.ConfigParser()
config.read(FILE)
config.sections()

API_KEY = config['CONFIG']['API_KEY']
NUMBER = config['CONFIG']['NUMBER']
SENDER = config['CONFIG']['SENDER']
TEAM = config['CONFIG']['TEAM']


