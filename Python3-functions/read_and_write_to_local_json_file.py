import json

def read_from_local_json_file(file_path):
	with open(file_path, 'r') as f:
		return json.load(f)

def write_into_local_json_file(file_path,data):
	with open(file_path, 'w') as f:
		json.dump(data, f)
