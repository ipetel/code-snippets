"""
#            .___    .___               __________        __         .__
#            |   | __| _/____    ____   \______   \ _____/  |_  ____ |  |
#            |   |/ __ |\__  \  /    \   |     ___// __ \   __\/ __ \|  |
#            |   / /_/ | / __ \|   |  \  |    |   \  ___/|  | \  ___/|  |__
#            |___\____ |(____  /___|  /  |____|    \___  >__|  \___  >____/
#                    \/     \/     \/                 \/          \/
#
Code Description:       Write Data into File
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


# ___ Write List of strings into CSV file
# assuming list of strings that each of them ends with '\n'

@try_except_decorator
def write_object_into_csv(file_path,data):
    with open(file_path, 'w') as f:
        f.writelines(data)
    
file_path = 'file_1.csv'
data = ['a1\n','b2\n','c3\n']
#write_object_into_csv(file_path,data)


# ___ Write List/Dict into JSON file
import json

@try_except_decorator
def write_object_into_json(file_path,data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

file_path = 'file_1.json'
data = [{'name':'a1\n'},{'name':'b2\n'},{'name':'c3\n'}]
write_object_into_json(file_path,data)
