'''
  this function creates Presigned URL for object stored in S3 bucket to unauthorized user for temporary time.
  more info:
    1) https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
    2) https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#object
    
  NOTICE: the service that creates this Presigned URL needs to have a permission to the action that given in the URL.
          for example, let's say that you are using AWS Lambda function to create this URL and you want to give 'get_object'
          permission, so this Lambda needs to have this permission before creating the URL
'''

import boto3

s3_client = boto3.client('s3')

def create_presigned_url(bucket_name, obj_key, expiration):
	try:
		response = s3_client.generate_presigned_url(
			ClientMethod='get_object',
			Params={'Bucket': bucket_name,'Key': obj_key},
			ExpiresIn=expiration,
			HttpMethod='GET'
		)
		
		return response
	except Exception as e:
		msg=f'### ERROR - {e}'
		print(msg)
		raise e
