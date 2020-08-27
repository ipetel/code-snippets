# this will overwrite the file if it already existed
import boto3
s3_resource = boto3.resource('s3')

def write_data_to_s3(s3_bucket_name,obj_key,payload):
	try:
		source_bucket_resource = s3_resource.Bucket(s3_bucket_name)
		
		response = source_bucket_resource.put_object(
			Body = payload,
			Key = obj_key
		)
		
		print(f'response: {response}')
	except Exception as e:
		msg=f'### ERROR - {e}'
		print(msg)
		raise e
