'''
  this function sends simple mail using verified email
  Notice:
    1) The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation will result in an "Email address not verified" error.
    2) The maximum message size is 10 MB.
    3) The message may not include more than 50 recipients
  for more info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_email
'''

import boto3

def send_mail_via_ses_service(email_from,email_to,email_body,email_subject):
	try:	
		client = boto3.client('ses')
		return client.send_email(
			Source=email_from,
			Destination={'ToAddresses':email_to},
			Message={
						'Body':{
							'Text':{
								'Data':email_body,
								'Charset': 'UTF-8'
							},
						},
						'Subject':{
							'Charset': 'UTF-8',
							'Data': email_subject
						}
					}
		)
	except ValueError:
		print(f'[### ERROR] - while trying to read from "{s3_obj_key}" file - error message: {ValueError}')
		return None
    
email_to=['example1@gmail.com','example2@gmail.com'] #list of email addresses
email_from='<SOURCE EMAIL>'
email_subject='<EMAIL SUBJECT>'
email_body='<EMAIL BODY>'
send_mail_via_ses_service(email_from,email_to,email_body,email_subject)
