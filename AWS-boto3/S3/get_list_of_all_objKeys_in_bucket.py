import boto3

def get_all_obj_in_bucket(bucket_name):
  try:
    s3_resource = boto3.resource('s3')
    bucket_resource = s3_client.Bucket(bucket_name)

    return [f.key for f in bucket_resource.objects.all()]
  except Exception as e:
    print(f'[### ERROR] - while trying to read file list of "{bucket_name}" - error message: {e}')
    raise e
    
def get_all_obj_in_bucket('example-bucket'):
