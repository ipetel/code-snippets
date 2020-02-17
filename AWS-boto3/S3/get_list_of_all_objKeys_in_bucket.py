import boto3

s3_client = boto3.resource('s3')
bucket_resource = s3_client.Bucket('<BUCKET-NAME>')

file_list= [f.key for f in bucket_resource.objects.all()]
