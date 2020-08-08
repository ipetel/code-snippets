import boto3
import datetime as dt
import pytz
import json

client = boto3.client('iot-data')

body = 'this is the body message'
current_ts = dt.datetime.now(pytz.utc).timestamp()

res= client.publish(
	topic='topics/topic_1',
	payload=json.dumps({'unix_ts':current_ts,'img':body})
	)
