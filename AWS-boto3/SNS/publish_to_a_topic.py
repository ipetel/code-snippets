sns_resource = boto3.resource('sns')

def publish_to_sns_topic(topic_arn,subject,msg):
	try:
		topic = sns_resource.Topic(topic_arn)
		response = topic.publish(
			Message=msg,
			Subject=subject,
		)
	except Exception as e:
		msg=f'### ERROR - {e}'
		print(msg)
		raise e
