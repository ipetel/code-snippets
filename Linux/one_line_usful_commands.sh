# read last line in file (you can change the number after "-n" to see last x rows)
  tail -n1 -f <FILE_PATH/FILE_NAME>

# truncate a file 
  truncate -s 0 <FILE_PATH/FILE_NAME>

# watch "top" for specific command
#example for <COMMAND_NAME> = python3
  top -c -p $(pgrep -d',' -f <COMMAND_NAME>)

# look for file name that start with "abc" from the current path
  find . -name abc*
  find <PATH / . > -type d -name "*<FOLDER-YOU-ARE-LOOKING>*" -print

#_________________________ Ububtu __________________________________________________

#### search for only installed packages using apt
  example: sudo apt list -a --installed <PART-OF-PACKAGE-NAME>*
  example: sudo apt list -a --installed libstdc++*

#### symbolic link (symlink)
  #create new link
  sudo ln -s /usr/bin/python3.5 /usr/bin/python3

  #create update an existed link
  ls -l /usr/bin/python3
  sudo ln -sf /usr/bin/python3.5 /usr/bin/python3

#### look for a string in many files
  grep -r '<STRING>' <PATH>
  example: grep -r 'python3' ~/*

#### replace new string with new one
  find <PATH-TO-SEARCH> -type f -exec sed -i 's/BAZEL_VERSION="3.1.0"/BAZEL_VERSION="3.4.1"/g' {} +
  find ~/* -type f -exec sed -i 's/<OLD-STRING>/<NEW-STRING>/g' {} +
