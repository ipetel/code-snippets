import boto3

try:
  s3_client = boto3.resource('s3')
  bucket_resource = s3_client.Bucket('<BUCKET-NAME>')

  file_list= [f.key for f in bucket_resource.objects.all()]
except ValueError:
  print(f'[### ERROR] - while trying to read file list of "{bucket_name}" - error message: {ValueError}')
  return None
