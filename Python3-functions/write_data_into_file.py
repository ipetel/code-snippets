'''
  this code is a general way to write data into file.
'''

### write file to txt
new_path = '<FILE-PATH>'
file_1 = open(new_path,'w')
file_1.write(file_list)
file_1.close()


### write file as JSON
import json

file_list=['a','b','c']

with open('file_list.json', 'w') as outfile:
    json.dump(file_list, outfile)
