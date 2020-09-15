# simple example for loop alphabetically + range of numbers with step
for x in {a..z}; do
  for y in {10..100..5}; do
      echo $x$y; 
      echo -e "\n"
  done >> ~/logs.txt
done
