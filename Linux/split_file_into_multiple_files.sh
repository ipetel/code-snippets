# This code will split every file that above the "max_size" value (in Bytes) 
# in "dir_path" folder and delete the original file

dir_path=/home/ubuntu/tmp/*;
max_size=104857600; #100MB in Bytes
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
