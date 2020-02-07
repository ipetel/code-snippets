from os.path import isfile, join
from os import listdir

files_path = '<FOLDER-PATH>'
#list of all files in the path
onlyfiles = [f for f in listdir(files_path) if isfile(join(files_path, f))]
# print count of element in a list 
print('num of files in folder:',len(onlyfiles))
