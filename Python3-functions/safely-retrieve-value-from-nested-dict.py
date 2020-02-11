'''
	get value from Dict in safe way - this function includes a simple example to understand how to use it.
'''
import json

data_json='{"key_10":{"key_20":{"key_30":11,"key_31":"None","key_32":{"key_40":"qwe","key_41":"ewq"}},"key_21":{"key_30":22,"key_31":33}},"key_11":"abcd"}';
data_dict=json.loads(data_json)

def get_val_from_dict_by_key_list(data_dict,key_list):
	if isinstance(data_dict,dict):
		dynamic_dict_path=data_dict
		for key in key_list:
			print(key)
			if isinstance(dynamic_dict_path,str):
				dynamic_dict_path=json.loads(dynamic_dict_path)

			if isinstance(dynamic_dict_path, dict) and key in dynamic_dict_path:
				dynamic_dict_path=dynamic_dict_path[key]
			elif isinstance(dynamic_dict_path, list) and len(dynamic_dict_path)>=int(key):
				dynamic_dict_path = dynamic_dict_path[key]
			else:
				print('key "{}" is not exists in this level, the keys available are: {}'.format(key,list(dynamic_dict_path.keys())))
				return None  

		return dynamic_dict_path
	else:
		print('"data_dict" is not "dict" type!')
		return None

val_needed=get_val_from_dict_by_key_list(data_dict,['key_10','key_20','key_32','key_41'])
print(val_needed)
