import boto3

def get_dynamodb_primary_key_list(table_name,partition_key,region):
	try:
		dynamodb_resource = boto3.resource('dynamodb',region_name=region)
		table = dynamodb_resource.Table(table_name)
		
		response = table.scan(
			Select='SPECIFIC_ATTRIBUTES',
			ProjectionExpression=partition_key
		)
		
		if 'Count' in response and response['Count']>0:
			return [x['file_name'] for x in response['Items']]
		else:
			print(f'[### ERROR] - dynamodb table "{table_name}" scan return empty response')
			return None
		
		print(f'get_dynamodb_primary_key_list response: {type(response)} | {response}')
		
	except ValueError:
		print(f'[### ERROR] - while trying to read data from dynamodb table "{table_name}" - error message: {ValueError}')
		return None	 
