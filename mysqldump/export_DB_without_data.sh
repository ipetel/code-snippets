# The following example shows how to run mysqldump on a client and write the dump to a file.
# using this code I have connected to remote EC2 instance that have permission to the AWS Aurora Cluster.
# base on: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Exporting.NonRDSRepl.html#MySQL.Procedural.Exporting.NonRDSRepl.CopyData

# 1. connect to the EC2 using the Terminal
# 2. run the next command to create the dump file in the current folder:
  sudo mysqldump -h <DB-ENDPOINT> \
  -u <DB-USER> \
  -p \
  --no-data \
  --column-statistics=0 \
  --port=3306 \
  --single-transaction=true \
  --routines \
  --triggers \
  --databases <DB-NAME-TO-DUMP> > <DUMP-FILE-NAME>.sql
  
# 3. write or paste the user password and press "enter"   
# Note: the time for creating the dump is depending on the table count, it should not take too long.

# what is "column-statistics=0" ?
# in order to over come "Unknown table 'COLUMN_STATISTICS' in information_schema (1109)" error
# for more info go to: https://serverfault.com/questions/912162/mysqldump-throws-unknown-table-column-statistics-in-information-schema-1109
