'''
  this function is get an exisiting item from DynamoDB table, if the item is not existed, in the response the Key 'item' will missing.
  notice: I have used Lambda's "Environment variables" ==> os.environ['SOMETHING']
  for more info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.get_item
'''
import json, os, boto3

def update_existed_record_dynamodb(contactId,transcription,transcription_s3_path):
	try:	
		dynamodb = boto3.resource('dynamodb',region_name=os.environ['REGION'])
		table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
		
		return table.get_item(
			Key={'key_name':'key_val'},
			UpdateExpression='SET field1 = :val1, field2= :val2',
			ProjectionExpression='<NAME-OF-COLUMN-RETURN>'
		)
	except Exception as e:
		msg=f'### ERROR - {e}'
		print(msg)
		return msg
