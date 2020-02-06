# using AWS CLI: if you want to copy entire s3 bucket to other bucket or to your local machine
#
# for a full tutorial to copy bucket cross AWS accounts, read the next post: https://medium.com/tensult/copy-s3-bucket-objects-across-aws-accounts-e46c15c4b9e1

# run this commend in your command line to copy from one bucket to the other:
aws s3 sync s3://SOURCE-BUCKET-NAME s3://DESTINATION-BUCKET-NAME --source-region SOURCE-REGION-NAME --region DESTINATION-REGION-NAME

#run this commmend in your command line to copy from an S3 bucket to local machine in specific path:
aws s3 sync s3://SOURCE-BUCKET-NAME /Users/some_name/folder1/ --source-region SOURCE-REGION-NAME
