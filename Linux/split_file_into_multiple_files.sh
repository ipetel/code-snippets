# This code will split every file that above the "max_size" value (in Bytes) 
# in "dir_path" folder and delete the original file

dir_path=/home/ubuntu/tmp/*;
max_size=104857600; #100MB in Bytes
#max_size=524288000; #500MB in Bytes
for file in $dir_path; do 
    file_size=$(wc -c <"$file")
    if [ $file_size -gt $max_size ]; then
        echo "$file size is over 100MB - start spliting the file...";
        split -d -b "$max_size" -a 4 "$file" "$file".;
        rm "$file";
    else
        echo "$file size is under 100MB";
    fi
done



# the following code will take CSV file and split it to new files with fix and given number of lines, in addtion it will have the header on each file
# https://www.baeldung.com/linux/split-file-with-header

tail -n +2 <SOURCE_FILE_PATH> | split -d -l <NUM_OF_LINES_FOR_EACH_FILE> - --filter='sh -c "{ head -n1 <SOURCE_FILE_PATH>; cat; } > $FILE"' <OUTPUT_FILES_STRUCTURE>

# <NUM_OF_LINES_FOR_EACH_FILE> => for example: 5
# <OUTPUT_FILES_STRUCTURE> => for example: some_path/input_data_
# <SOURCE_FILE_PATH> => for example: some_path/input_file.csv
