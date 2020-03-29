import boto3
from boto3.dynamodb.conditions import Key, Attr

def get_dynamodb_records_with_initiated_status(table_name,region):
	try:
		dynamodb_resource = boto3.resource('dynamodb',region_name=region)
		table = dynamodb_resource.Table(table_name)
		
		response = table.scan(
		    Select='SPECIFIC_ATTRIBUTES',
		    ProjectionExpression='<FIELD-1>,<FIELD-2>,<FIELD-3>',    
		    FilterExpression=Attr('<FIELD-X>').eq('<FIELD-VALUE>')
		)
		
		print(f'response: {response}')
	except ValueError:
		print(f'[### ERROR] - while trying to scan dynamodb table "{table_name}" - error message: {ValueError}')
		return None	
