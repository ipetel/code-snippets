import sys
import time

### init params

start_time = time.time()
logFile_name='subprocess_running.log'

### functions

def write_to_log_file(logFile_name, msg):
	file_object = open(logFile_name, 'a')
	file_object.write(str(msg))
	file_object.close()

### main 

def main():
	# get inputs from main script
	input_1 = int(sys.argv[1])
	input_2 = int(sys.argv[2])
	pid = int(sys.argv[3])

	total_num=0
	for i in range(input_1,input_2):
		total_num += i

		# monitor process - write to log file and print
		percentage=round(((i-input_1)/(input_2-input_1))*100,3)
		msg='pid {}: processed {}% of files\n'.format(pid,percentage)
		write_to_log_file(logFile_name,msg)
		
	# monitor process - write to log file and print 
	msg='pid {}: process is DONE in {} sec, the resualt is {}\n'.format(pid,round(time.time()-start_time,2),total_num)
	write_to_log_file(logFile_name,msg)

if __name__ == "__main__":
	main()
