"""
#            .___    .___               __________        __         .__
#            |   | __| _/____    ____   \______   \ _____/  |_  ____ |  |
#            |   |/ __ |\__  \  /    \   |     ___// __ \   __\/ __ \|  |
#            |   / /_/ | / __ \|   |  \  |    |   \  ___/|  | \  ___/|  |__
#            |___\____ |(____  /___|  /  |____|    \___  >__|  \___  >____/
#                    \/     \/     \/                 \/          \/
#
Code Description:       Read Data From File
Auther:                 Idan Petel
Date:                   Dec 2020
Version:                1.0
Script Logic:           None
Environment Variables:  None
"""

import logging
from pprint import pprint
from functools import wraps


# ___ logging config
LOG_LEVEL = logging.INFO
logging.basicConfig(level=LOG_LEVEL, format='### %(levelname)s ### - line: %(lineno)s, msg: %(message)s')
logger = logging.getLogger()


# ___ function_decorator
def try_except_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            response = function(*args, **kwargs)
            logger.info(f'{function.__name__}() function operation was completed successfully')
            return response
        except Exception as err:
            logger.error(f'{err}')
    return wrapper


# ___ Load CSV file into list of dicts
# assuming file first line is headers
from csv import DictReader

@try_except_decorator
def load_csv_file_into_list_of_dicts(file_path):
    with open(file_path, 'r') as f:
        return [{k: v for k, v in row.items()} for row in DictReader(f, skipinitialspace=True)]
    
file_path = 'file_1.csv'
data = load_csv_file_into_list_of_dicts(file_path)

# print the first 2 dicts in the list
pprint(data[:2])


# ___ read JSON file into Python object (NOT JSON LINES!)
import json

@try_except_decorator
def load_json_file_into_python_object(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

file_path = 'file_2.json'
data = load_json_file_into_python_object(file_path)

# print the data
pprint(data)


# ___ read from txt file line by line
# example file:
#   abcd
#   asdf
#   vfffr

@try_except_decorator
def read_file_line_by_line(file_path):
	with open(file_path) as f:
	    return [line.rstrip() for line in f]
	
file_path = 'file_3.txt'
data = read_file_line_by_line(file_path)

# print the data
pprint(data)
