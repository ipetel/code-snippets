'''
  Thid function is for reading simple JSON file from S3 bucket
'''
import json, boto3

def read_object_from_s3_bucket(s3_obj_key,bucket_name):
    try:
        s3_client = boto3.resource('s3')
        source_bucket_resource = s3_client.Bucket(bucket_name)
        content_object = source_bucket_resource.Object(s3_obj_key)
    
        #collected data in the form of bytes array + Decode it in 'utf-8' format
        file_content = content_object.get()['Body'].read().decode('utf-8')
        
        return json.loads(file_content)
    except ValueError:
        print(f'[### ERROR] - while trying to read from "{s3_obj_key}" file - error message: {ValueError}')
        return None
