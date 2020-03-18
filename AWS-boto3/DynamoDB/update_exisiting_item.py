'''
  this function is updating an exisiting item in DynamoDB table, if the item is not existed it will add the record as insert.
  notice: I have used Lambda's "Environment variables" ==> os.environ['SOMETHING']
'''
import json, os, boto3

def update_existed_record_dynamodb(contactId,transcription,transcription_s3_path):
	try:	
		dynamodb = boto3.resource('dynamodb',region_name=os.environ['REGION'])
		table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
		
		return table.update_item(
			Key={'key_name':'key_val'},
			UpdateExpression='SET field1 = :val1, field2= :val2',
			ExpressionAttributeValues={':val1':123,':val2':456}
		)
	except Exception as e:
		msg=f'### ERROR - {e}'
		print(msg)
		return msg
