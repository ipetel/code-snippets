'''
  this function is get an exisiting item from DynamoDB table, if the item is not existed, in the response the Key 'item' will missing.
  notice: I have used Lambda's "Environment variables" ==> os.environ['SOMETHING']
  for more info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.get_item
'''
import json, os, boto3

dynamodb_resource = boto3.resource('dynamodb',region_name=os.environ['REGION'])
dynamodb_table_name = os.environ['DYNAMODB_TABLE']

def update_existed_record_dynamodb(dynamodb_table_name,key_val):
	try:	
		table = dynamodb.Table()
		
		response = table.get_item(
			Key={'key_name':key_val},
			ProjectionExpression='<NAME-OF-COLUMN-RETURN>'
		)
		
		return response.get('Item',None)
	except Exception as e:
		msg=f'### ERROR - {e}'
		print(msg)
		raise e
