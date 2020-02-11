# read last line in file (you can change the number after "-n" to see last x rows)
tail -n1 -f <FILE_PATH/FILE_NAME>

# truncate a file 
truncate -s 0 <FILE_PATH/FILE_NAME>

# watch "top" for specific command
#example for <COMMAND_NAME> = python3
top -c -p $(pgrep -d',' -f <COMMAND_NAME>)
