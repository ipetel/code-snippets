# This script using 'mysqlslap' that is a tool for load-testing MariaDB. It allows you to emulate multiple concurrent connections, and run a set of queries multiple times. 
# for more info: https://mariadb.com/kb/en/mysqlslap/

# Simple example run on Terminal:
mysqlslap -h <DB-ENDPOINT> -u<DB-USER> -p<DB-PWD> --create-schema=mysql -q 'select user,host from mysql.user limit 1;' --concurrency=40 --number-of-queries=10000000000;
