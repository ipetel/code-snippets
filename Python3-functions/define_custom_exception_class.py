'''
This code is a simple example how to define custom exception class in Python
'''

# custom exception class
class CustomError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
        

# use it whenever you need in your code as follows:
    try:
      ...
      <some code>
      ...
  	except Exception as e:
		  print(f'### [ERROR] - {e}')
		  raise CustomError('some error message')
