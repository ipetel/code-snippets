### Managing Multiple Python Versions With pyenv

https://realpython.com/intro-to-pyenv/#:~:text=pyenv%20is%20a%20wonderful%20tool,a%20different%20version%20of%20Python.
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
