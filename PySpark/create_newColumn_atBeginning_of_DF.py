from pyspark.sql.functions import lit

# option 1
df = df.select(lit('value').alias("new_column_header"), "*")

# option 2 - example of using other col that in unix time and convert it into datetime format
df_2 = df.withColumn("<NEW-COL-NAME>", F.from_unixtime("epoch_timestamp"))
