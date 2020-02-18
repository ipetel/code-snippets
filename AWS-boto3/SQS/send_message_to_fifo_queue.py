'''
  for more info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message
'''

import json, boto3

queue_url='<QUEUE-URL>'
sqs_client = boto3.client('sqs',region_name='<REGION-NAME>')

# functions 
def send_mesage_to_sqs_queue(msg,some_id):
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(msg),
        MessageGroupId='general_group',
        MessageDeduplicationId=some_id
    )
    response_statusCode=get_val_from_dict_by_key_list(response,['ResponseMetadata','HTTPStatusCode'])
    
    if response_statusCode==200:
       print(f'[@@@ INFO] - {msg} was sent successfully')
    else:
        print(f'[### ERROR] - {msg} was fail to sent to Queue')

some_id = '<MESSAGE-ID-FOR-DEDUPLICATION>'
msg={'data':'some contact'}
send_mesage_to_sqs_queue(msg,some_id)
