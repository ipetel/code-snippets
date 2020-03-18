'''
	this function is invoke by S3 Events on new object in the bucket, and get the buxket name and the object key
	
	there is a use of 'unquote' function due to auto encoding by AWS (I assume), for example:
	in the S3 bucket the name of the file is: 6ecea53-2531-4375-af4d-f98027a88825_2020-03-18T10:06:41.635+0000_AUDIO_FROM_CUSTOMER.wav
	but in the Lambda's 'event' parameter the name received: e6ecea53-2531-4375-af4d-f98027a88825_2020-03-18T10%3A06%3A41.635%2B0000_AUDIO_FROM_CUSTOMER.wav
	and when trying to read this file, you will get an Error that this object is not existed in the bucket.
'''

import json
from urllib.parse import unquote

### functions

def get_val_from_dict_by_key_list(data_dict,key_list):
	if isinstance(data_dict,dict):
		dynamic_dict_path=data_dict
		for key in key_list:
			#print('[@@@ INFO] - ',key)
			if isinstance(dynamic_dict_path,str):
				dynamic_dict_path=json.loads(dynamic_dict_path)

			if isinstance(dynamic_dict_path, dict) and key in dynamic_dict_path:
				dynamic_dict_path=dynamic_dict_path[key]
			elif isinstance(dynamic_dict_path, list) and len(dynamic_dict_path)>=int(key):
				dynamic_dict_path = dynamic_dict_path[key]
			else:
				print('[### ERROR] - key "{}" is not exists in this level, the keys available are: {}'.format(key,list(dynamic_dict_path.keys())))
				return None  

		return dynamic_dict_path
	else:
		print('[### ERROR] - "data_dict" is not "dict" type!')
		return None

### main

def lambda_handler(event, context):
	bucket_name_input=get_val_from_dict_by_key_list(event,['Records',0,'s3','bucket','name'])
	obj_key=unquote(get_val_from_dict_by_key_list(event,['Records',0,'s3','object','key']))

  return {
    'statusCode': 200,
    'body': json.dumps(f'{bucket_name_input}/{obj_key}', default=str)
  }
