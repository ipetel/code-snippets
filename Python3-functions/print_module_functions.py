'''
  This code is to print all functions define to python module, here is the example for printing all "Pandas" functions that are not starting with 2 underscores.
'''
import pandas as pd

method_list = [func for func in dir(pd) if callable(getattr(pd, func)) and not func.startswith("__")]
print(method_list)
