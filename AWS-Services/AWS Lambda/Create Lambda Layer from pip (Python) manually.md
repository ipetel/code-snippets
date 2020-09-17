# Create Lambda Layer

### Creating AWS Lambda Layer with Terraform
- https://medium.com/@ipetel/creating-aws-lambda-layer-with-terraform-in-3min-ae49a80d38c

### The Manually Way (Python 3.8)
1) ssh into the EC2 instance (this instance has to have AMI permission to write to S3).
1) Make sure that the python version you are creating the layer to is the python that installed in the instance.
1) make sure python3 and pip3 are installed.
1) make sure/create a folder structure like this: `mkdir -p ~/build/python/lib/python3.8/site-packages`
1) install the package to specific destination folder: `pip3 install <package-name> -t ~/build/python/lib/python3.8/site-packages/`
1) *** You can delete the ‘.dist-info’ folder and ‘__pychace__’ folder
1) cd into `~/build` folder (meaning you zip the ‘python’ folder)
1) zip the `python` folder `zip -r <zip_name>.zip .`
1) copy package zip into s3 bucket `aws s3 cp <package-name>.zip s3://<bucket-name>/<zip_file_name>`
1) copy ARN path of zip object from the S3 bucket.
1) create a new layer using the copied ARN path.
1) in the Lambda function use a new layer `Import <package-name>`
