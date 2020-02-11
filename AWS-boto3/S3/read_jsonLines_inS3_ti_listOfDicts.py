import json
import boto3

'''
  this function handle reading json lines file from S3 bucket into list of dict
'''

def get_jsonLines_object_dataContent(object_key,bucket_resource):
  content_object = bucket_resource.Object(object_key)

  #collected data in the form of bytes array + Decode it in 'utf-8' format
  file_content = content_object.get()['Body'].read().decode('utf-8')

  #StringIO object
  stringio_data = io.StringIO(file_content)

  #read the StringIO obj line by line.
  data = stringio_data.readlines()

  #Its time to use json module now.
  json_data = list(map(json.loads, data))

  return json_data

object_key= '<S3-FILE-PATH>/<FILE-NAME>'
s3_client = boto3.resource('s3')
bucket_resource = s3_client.Bucket('<BUCKET-NAME>')
get_jsonLines_object_dataContent(object_key,bucket_resource)
