  
'''
  Batch insert / delete from "table_1", asumme that the table Primary key/Partition key is "key_1"

  
'''

import logging
from functools import wraps
import boto3

# ___ boto3 init

dynamodb = boto3.resource('dynamodb')

# ___ Decorators

def try_except(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        try:
            response = orig_func(*args, **kwargs)
            logging.info(f'{orig_func.__name__}() function operation was completed successfully')
            return response
        except Exception as err:
            logging.error(f'{err}')
    return wrapper

@try_except
def insert_items_in_batch():
  table_name = 'table_1'
  table = dynamodb.Table(table_name)
  
      with table.batch_writer() as batch:
        for i in range(1,1000):
            batch.put_item(Item={'key_1':i,'key_2':'ABCD','key_3':{'a1':'b1','a2':4}})

@try_except
def delete_items_in_batch():
  table_name = 'table_1'
  table = dynamodb.Table(table_name)
  
      with table.batch_writer() as batch:
        for i in range(1,1000):
            batch.delete_item(Key={"key_1":i})
    
