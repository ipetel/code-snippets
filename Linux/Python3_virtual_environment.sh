# refrence: https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-python3-boto3/

#If Python 3 isn't already installed
sudo yum install python3 -y

# Create a virtual environment on the current folder (You can change my_app to another name)
python3 -m venv my_app/env

#Activate the environment
source ~/my_app/env/bin/activate

#install last pip module
pip install pip --upgrade
