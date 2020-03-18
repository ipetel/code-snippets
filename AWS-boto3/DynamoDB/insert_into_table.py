'''
	simple code to put a new record into dynamodb table
  (don't forget that one of the value have to be the table key)
'''

import boto3

try:
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('<TABLE NAME>')

	table.put_item( 
	      Item={'key_1':123,
		    'key_2':'ABCD',
		    'key_3':{'a1':'b1','a2':4}
		})
except Exception as e:
	msg=f'### ERROR - {e}'
	print(msg)
	return msg
