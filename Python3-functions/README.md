### Managing Multiple Python Versions With pyenv
https://realpython.com/intro-to-pyenv/

Prerequisites:
1) install pyenv
1) install pyenv-virtualenv

Env setup:
1) get a list of available Python versions: ```pyenv install --list``` 
1) install a specific version: ```pyenv install -v 3.8.5``` 
1) create virtualenv with a specific Python version: ```pyenv virtualenv 3.8.5 my_app```
1) activate the new virtualenv in the current terminal: ```pyenv shell my_app```
1) check what version is being used: ```pyenv versions```
 
___________________________________________________________________________________

### create a Python 3 virtual environment with the Boto 3 library on Amazon Linux 2

https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-python3-boto3/
___________________________________________________________________________________

### Install PIP

1) wget -nv https://bootstrap.pypa.io/get-pip.py
2) python3 get-pip.py
___________________________________________________________________________________

### Error Handling

```python
try:
     .....
except Exception as e:
     msg=f'### ERROR - {e}'
     print(msg)
     raise e
```
