'''
  this code copy object from one bucket to other bucket
'''

import boto3
s3_client = boto3.resource('s3')
source_bucket_name='<BUCKET-NAME-1>'
target_bucket_name='<BUCKET-NAME-2>'
s3_obj_key='a/b/data.json'

copy_source = {'Bucket': source_bucket_name,'Key': s3_obj_key}
s3_client.Bucket(target_bucket_name).copy(copy_source, s3_obj_key)
