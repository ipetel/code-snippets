# The following example shows how to import data into MySQL using dump file.
# using this code I have connected to remote EC2 instance that have permission to the AWS Aurora Cluster.
# this EC2 instance contains mysqldump file: "dump-file-1.sql" in the Home folder.

# 1. connect to the EC2 using the Terminal
# 2. connect to the RDS instance using the next command:
# Note: you will need to connect to the WRITER instance not READER!
mysql -h <DB-ENDPOINT> -P 3306 -u <DB-USER> -p
# 3. write or paste the user password and press "enter"
# 4. now you are connected to the DB and can run SQL queries in the Terminal.

#if you are migrate to the same DB name
# 5. run the next queries:
CREATE DATABASE <SOURCE-DB-NAME>;
USE <SOURCE-DB-NAME>;
source "dump-file-1.sql";

#else, you are migrate to different DB name 
# 5. you will need to run this command in the EC2 instance Terminal (exit from the DB):
sed -i 's/<SOURCE-DB-NAME>/<DEST-DB-NAME>/g' "dump-file-1.sql"
# 6. connect to the RDS instance using the next command (again):
# Note: you will need to connect to the WRITER instance not READER!
mysql -h <DB-ENDPOINT> -P 3306 -u <DB-USER> -p
# 7. write or paste the user password and press "enter"
# 8. run the next queries:
CREATE DATABASE <DEST-DB-NAME>;
USE <DEST-DB-NAME>;
source "dump-file-1.sql";

# Troubleshooting
# When attempting to import data to Amazon RDS (MySQL) using mysqldump file, you received an error similar to the following:
# Definer error: example: /*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ 
# you will need to run this command in the EC2 instance Terminal (exit from the DB):
# sed -i -e 's/DEFINER=`root`@`localhost`//g' "dump-file-1.sql"
# for more info: https://aws.amazon.com/premiumsupport/knowledge-center/definer-error-mysqldump/
