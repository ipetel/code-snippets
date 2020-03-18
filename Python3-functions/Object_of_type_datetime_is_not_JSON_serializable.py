'''
  overcome the 'Object of type datetime is not JSON serializable' issue when using 'json.dumps' on object that contains datetime type 
  code reference: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
'''

json.dumps(my_dictionary, default=str)
