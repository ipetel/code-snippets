# Install
#  pip3 install psycopg2-binary (https://www.psycopg.org/docs/install.html#quick-install)

# Run
import psycopg2

con = psycopg2.connect(
dbname="<DB-NAME>",
host="<ENDPOINT-URL>",
port= 5439,
user="<DB-USER>",
password="<DB-PASSWORD>")

cur = con.cursor()

cur.execute("SELECT * FROM lineitem LIMIT 5")

records = cur.fetchall()

print(records)
