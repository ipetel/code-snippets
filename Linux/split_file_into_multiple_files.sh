# This code will split every file that above the "max_size" value in "dir_path" folder and delete the original file

max_size=500M;
dir_path=/home/ubuntu/tmp/;
for file in "$(find "$dir_path" -type f -size +"$max_size")"; do
    echo "$file";
    split -d -b "$max_size" -a 4 "$file" "$file".;
    rm "$file";
done
