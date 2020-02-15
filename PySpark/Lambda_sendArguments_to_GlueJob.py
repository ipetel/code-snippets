'''
  this script is for invoke Glue Job from Lambda function using Arguments by using boto3 SDK
  for more info: https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-get-resolved-options.html
'''

### in the Lambda function:

import boto3
glue_client = boto3.client('glue')
response = glue_client.start_job_run(
  JobName='<GLUE_JOB_NAME>',
  Arguments={'--KEY_1':'VAL_1','--KEY_2':'VAL_2'}
)

### in the Glue Job (PySpark)

args = getResolvedOptions(sys.argv, ['JOB_NAME','<KEY_1>','<KEY_2>'])
KEY_1_VAL=args['<KEY_1>']
