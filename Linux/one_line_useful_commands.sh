# read last line in file (you can change the number after "-n" to see last x rows)
  tail -n1 -f <FILE_PATH/FILE_NAME>

# truncate a file 
  truncate -s 0 <FILE_PATH/FILE_NAME>

# watch "top" for specific command
#example for <COMMAND_NAME> = python3
  top -c -p $(pgrep -d',' -f <COMMAND_NAME>)

# look for substring of a file name or folder
  find <PATH / . > -name "*<FOLDER-YOU-ARE-LOOKING>*" -print # file
  find <PATH / . > -type d -name "*<FOLDER-YOU-ARE-LOOKING>*" -print # folder
  
# ignore command output
cmd > /dev/null 2>&1

#_________________________ Ububtu __________________________________________________

#### search for only installed packages using apt
  sudo apt list -a --installed <PART-OF-PACKAGE-NAME>*
  example: sudo apt list -a --installed libstdc++*

#### symbolic link (symlink)
  # create new link
  sudo ln -s <LINK-TARGET-FILE> <LINK-FILE>
  sudo ln -s /usr/bin/python3.5 /usr/bin/python3

  # update an existed link (you can also delete the only one and just create a new instead)
  ls -l /usr/bin/python3
  sudo ln -sf /usr/bin/python3.5 /usr/bin/python3

#### look for a string in many files
  grep -r '<STRING>' <PATH>
  example: grep -r 'python3' ~/*

#### replace new string with new one
  find <PATH-TO-SEARCH> -type f -exec sed -i 's/BAZEL_VERSION="3.1.0"/BAZEL_VERSION="3.4.1"/g' {} +
  find ~/* -type f -exec sed -i 's/<OLD-STRING>/<NEW-STRING>/g' {} +
  
#### split file to many small files of 1GB size + delete the original file
  split -d -b 1G -a 4 <ORIGINAL-FILE-PATH> <ORIGINAL-FILE-PATH>. && rm <ORIGINAL-FILE-PATH>
