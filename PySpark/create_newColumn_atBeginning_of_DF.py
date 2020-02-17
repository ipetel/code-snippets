from pyspark.sql.functions import lit

df = df.select(lit('value').alias("new_column_header"), "*")
