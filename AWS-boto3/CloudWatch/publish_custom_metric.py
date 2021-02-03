
# ===================================================================================================
#                    .___    .___               __________        __         .__
#                    |   | __| _/____    ____   \______   \ _____/  |_  ____ |  |
#                    |   |/ __ |\__  \  /    \   |     ___// __ \   __\/ __ \|  |
#                    |   / /_/ | / __ \|   |  \  |    |   \  ___/|  | \  ___/|  |__
#                    |___\____ |(____  /___|__/  |____|    \_____>__|  \_____>____/                   
#
#
# Code Description:       publish a custom metric to AWS CloudWatch
#                         https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data
# Script Logic:           None
# Environment Variables:  None
#
# Auther:                 Idan Petel
# Date:                   Feb 2021
# Version:                1.0
# ===================================================================================================

from functools import wraps
import logging
import boto3
from datetime import datetime

client = boto3.client('cloudwatch')

# ___ logging config
LOG_LEVEL = logging.DEBUG
logging.basicConfig(level=LOG_LEVEL, format='### %(levelname)s ### - line: %(lineno)s, function: %(funcName)s(), msg: %(message)s')

# ___ Decorators
def try_except_decorator(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        try:
            response = orig_func(*args, **kwargs)
            logger.info(f'{orig_func.__name__}() function operation was completed successfully')
            return response
        except Exception as err:
            logger.error(f'{err}')
    return wrapper
    
# ___ Function

@try_except_decorator
def publish_custom_metric_to_cloudwatch(metric_name,metric_value,metric_unit,subsystem_name):
    return client.put_metric_data(
        Namespace=f'customMetric/{metric_name}',
        MetricData=[
            {
                'MetricName': metric_name,
                'Dimensions':[
                    {
                        'Name': 'Subsystem',
                        'Value': subsystem_name
                    },
                ],
                'Timestamp': datetime.now(),
                'Value': metric_value,
                'Unit': metric_unit,
                'StorageResolution': 60
            },
        ]
    )
    
# ___ Main
subsystem_name = 'subsystem_1'
metric_name = 'custom_metric_1'
metric_value = 123.4
metric_unit = 'Seconds'
response=publish_custom_metric_to_cloudwatch(metric_name,metric_value,metric_unit,subsystem_name)
