# The following example shows how to run mysqldump on a client and write the dump to a file.
# using this code I have connected to remote EC2 instance that have permission to the AWS Aurora Cluster.
# base on: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Exporting.NonRDSRepl.html#MySQL.Procedural.Exporting.NonRDSRepl.CopyData

# 1. connect to the EC2 using the Terminal
# 2. run the next command to create the dump file in the current folder:
  sudo mysqldump -h <DB-ENDPOINT> \
  -u <DB-USER> \
  -p<DB-PASSWORD> \
  --verbose
  --port=3306 \
  --single-transaction=true \
  --routines \
  --triggers \
  --databases <DB-NAME-TO-DUMP> > <DUMP-FILE-NAME>.sql
# 3. write or paste the user password and press "enter"   

# Note: the time for creating the dump is depending on the DB size, I have used a small DB (40GB) that took around 30min.   

#________________________________________________________________________________________________________________________________________________

# export DBinto gzip file

  sudo mysqldump -h <DB-ENDPOINT> \
  -u <DB-USER> \
  -p<DB-PASSWORD> \
  --verbose
  --port=3306 \
  --single-transaction=true \
  --routines \
  --triggers \
  --databases <DB-NAME-TO-DUMP | gzip > <DUMP-FILE-NAME>.sql.gz
  
  # when doing mysqldump from RDS you will need to change the owner of the table after unzip it
  sed -i 's/DEFINER=[^*]*\*/\*/g' <DUMP-FILE-NAME>.sql 
