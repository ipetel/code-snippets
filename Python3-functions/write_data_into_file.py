'''
  this code is a general way to erite data into file, in this example it is shown on JSON file.
'''

import json

file_list=['a','b','c']

with open('file_list.json', 'w') as outfile:
    json.dump(file_list, outfile)
