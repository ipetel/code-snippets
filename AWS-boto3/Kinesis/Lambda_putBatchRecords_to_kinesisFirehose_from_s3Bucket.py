'''
  This code uses AWS boto3 in Lambda function to put records in batch mode into Kinesis Firehose, 
  the source of the data is from S3 bucket.
  
  # Firehose
    1) I will use "PutRecordBatch", notice that each PutRecordBatch request supports up to 500 records.
       so I will need to split the calls because each file contains more than 500 records (for the files I used).
    2) notice that the data structure for "PutRecordBatch" is [{"Data":<PAYLOAD>},{"Data":<PAYLOAD>},...]
       the <PAYLOAD> needs to be b'bytes' type, I used json.dumps function to comvert the dict to json (string)
    3) the <PAYLOAD> maximum size, before base64-encoding, is 1,000 KiB.
  
  # S3
    the data in the bucket is in JSON format (this is what I used)

  # data flow illustration
    S3 --read--> Lambda --write--> Firehose 
'''

import boto3
import json
import io

### init params

firehose_client = boto3.client('firehose',region_name='<FIREHOSE_REGION>')
s3_client = boto3.resource('s3',region_name='<S3_REGION>')

# Each PutRecordBatch request supports up to 500 records
# for more info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.put_record_batch
max_records_per_call=500

### functions

def get_list_of_all_objectsKeys_forGiven_s3_bucket(bucket_resource):
	'''
    this function uses boto3 on s3 resource on specific S3 bucket
    to return a list of all objects keys (path) in the bucket using list comprehension 
	'''
	return [x.key for x in bucket_resource.objects.all()]

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

def split_list_into_nSize_lists(data_list,N):
	'''
    this function split given list by using N value into small list in size of N.
	'''
	if isinstance(data_list,list):
		new_list=[]
		count_list_elem=len(data_list)
		num_of_sub_lists=round(count_list_elem/N)
		
		i=0
		while i <= num_of_sub_lists:
			offset=N*i
			new_list.append(data_list[offset:offset+N])
			i+=1
			
		return new_list
	else:
		print('ERROR - Data provide is not List type')
		return None

def organize_data_before_push_to_firehose(data):
	return [{"Data": json.dumps(x)} for x in data]

def send_batch_Data_to_Firehose(data):
	firehose_client.put_record_batch(
		DeliveryStreamName='<FIREHOSE_NAME>',
		Records=data
	)

### main	

def lambda_handler(event, context):
  bucket_resource = s3_client.Bucket('<BUCKET_NAME>')
  objectsKeys_list = get_list_of_all_objectsKeys_forGiven_s3_bucket(bucket_resource)
  
  pre_process_data=[]
  for x in objectsKeys_list:
    # concatenate lists
    pre_process_data += get_jsonLines_object_dataContent(x,bucket_resource)
    
  split_lists = split_list_into_nSize_lists(pre_process_data,max_records_per_call)
  
  for sub_list in split_lists:
    organized_data = organize_data_before_push_to_firehose(sub_list)
    send_batch_Data_to_Firehose(organized_data)
	
	return {
        'statusCode': 200,
        'body': 'DONE'
    }
