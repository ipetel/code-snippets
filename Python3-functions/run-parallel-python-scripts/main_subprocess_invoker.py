'''
	This script was created to run the same Python script multiple times with different inputs at the same time (parallel running) by using the 'subprocess' lib.
	for more info: https://docs.python.org/3.8/library/subprocess.html
	
	### real-time outputs from running subprocesses
	I have tried for hours to find a solution for getting realtime output to the main script, all the 'stack overflow' I found were with only with ONE subprocess running (not many).
	so I have created a workaround, each subprocess writes to the same log file and by using Unix command - "tail" I have mange to get real-time outputs from running subprocesses.
	here is the commend I have used: tail -n1 -f <LOG-FILE-NAME>

	### assumptions
	1) main Python script (file) - main_subprocess_invoker.py (this script), subprocess Python script (file) - subprocess_script.py, and the log file - subprocess_running.log are existed and are at the same folder path
	2) using a Linux based system when running this code (I have used My Mac)
	3) using Python 3 (I have ran it on version 3.7)
	4) notice that the log file need to be created before running the code, so create one before the first run -> subprocess_running.log

'''

import sys
from subprocess import Popen, PIPE
import time

### init params

start_time = time.time()
logFile_name='subprocess_running.log'
process_input_list = [{"start":0,"end":10}, {"start": 10, "end": 20}, {"start": 20, "end": 30}, {"start": 30, "end": 40}]
num_of_processes=4

### functions

def clear_log_file(logFile_name):
	file_object = open(logFile_name,"r+")
	file_object.truncate(0)
	file_object.close()

def write_to_log_file(logFile_name,msg):
	file_object = open(logFile_name, 'a')
	file_object.write(str(msg))
	file_object.close()

### main

def main():
	# delete previous runs
	clear_log_file(logFile_name)
	print('opening {} processes'.format(num_of_processes))

	# start creating and running the Python scripts
	process_list=[]

	for i in range(num_of_processes):
		# ['linux command','the script to run','pass param to script 1','pass param to script 2',,'pass param to script 3']
		process = Popen(['python3','subprocess_script_batchOf10.py','{}'.format(process_input_list[i]['start']),'{}'.format(process_input_list[i]['end']),'{}'.format(i)],shell=False, stdout=PIPE,stderr=PIPE,universal_newlines=True)
		print('start process {}'.format(i))
		process_list.append(process)

	# print running processes prints, this loops will continue running until all the processes will finish
	while True:
		print('.')

		if len(process_list)==0:
			break


		for p in process_list:
			msg=p.stdout.readline().rstrip()

			# if process have empty stdout and the poll()!=None ====> the process finished
			if msg == '' and p.poll() != None:
				process_list.remove(p)

	msg='main process is done in {} sec'.format(round(time.time()-start_time, 2))
	print(msg)
	write_to_log_file(logFile_name,msg)

if __name__ == "__main__":
    main()
