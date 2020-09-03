import boto3
s3_client = boto3.client('s3')

def get_the_files_to_process(s3_bucket_name,folder_path):
	try:
		response = s3_client.list_objects_v2(
			Bucket=s3_bucket_name,
			Prefix=folder_path,
		)
		#print(f'response:{response}')
		
		if response.get('Contents',None) is None:
			return None
		else:
			if len(response['Contents'])==0:
				return None
			else:
				return [x['Key'] for x in response['Contents']]
			
	except Exception as e:
		msg=f'### ERROR - {e}'
		print(msg)
		raise e
