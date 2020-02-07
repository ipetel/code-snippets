import boto3

bucket_name='<BUCKET-NAME>'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
file_list= [f for f in bucket.objects.all()]
print('num of files in bucket "{}":'.format(bucket_name),len(file_list))
