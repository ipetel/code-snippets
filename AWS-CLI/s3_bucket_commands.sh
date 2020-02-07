##### this code snippts is for using AWS CLI on S3 bucket #####


# if you want to copy entire s3 bucket to other bucket or to your local machine 
  
  # copy from one bucket to the other
  aws s3 sync s3://<SOURCE-BUCKET-NAME> s3://<DESTINATION-BUCKET-NAME>

  #copy from an S3 bucket to local machine in specific path
  aws s3 sync s3://<SOURCE-BUCKET-NAME> <LOCAL-FOLDER-PATH>

  # for a full tutorial to copy bucket cross AWS accounts
  #read the next post: https://medium.com/tensult/copy-s3-bucket-objects-across-aws-accounts-e46c15c4b9e1

  #copy from local to S3 bucket
  aws s3 sync <LOCAL-FOLDER-PATH> s3://<SOURCE-BUCKET-NAME>
  #you can use DEBUG flag to get feedback to the terminal
  aws s3 sync <LOCAL-FOLDER-PATH> s3://<SOURCE-BUCKET-NAME> --debug

# Get Stats on the S3 Bucket like Size and Number of Objects
  aws s3 ls s3://<SOURCE-BUCKET-NAME> --summarize --human-readable
