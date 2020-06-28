# USING "du" command to estimate file space usage
# https://www.geeksforgeeks.org/du-command-linux-examples/
#
#	-0, –null : end each output line with NULL
#	-a, –all : write count of all files, not just directories
#	–apparent-size : print apparent sizes, rather than disk usage.
#	-B, –block-size=SIZE : scale sizes to SIZE before printing on console
#	-c, –total : produce grand total
#	-d, –max-depth=N : print total for directory only if it is N or fewer levels below command line argument
#	-h, –human-readable : print sizes in human readable format
#	-S, -separate-dirs : for directories, don’t include size of subdirectories
#	-s, –summarize : display only total for each directory
#	–time : show time of last modification of any file or directory.
#	–exclude=PATTERN : exclude files that match PATTERN

#example of great command: 
du -h -d 1

