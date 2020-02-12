'''
  this code is for using PySpark to read straight from S3 bucket instead of using the default data source (AWS Glue Data Catalog).
'''

#this is the default line that we will change:
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "<DATABASE_NAME>", table_name = "<TABLE_NAME>", transformation_ctx = "datasource0")

# so replace the previous code with this:
obj_list = ['s3://<OBJECT_PATH>'] # list of all relevant objects 
datasource0 = glueContext.create_dynamic_frame_from_options(connection_type = "s3",connection_options={"paths": [obj_list]}, format = "csv", format_options={"withHeader": False,"separator": ","})

# for more info: https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-glue-context.html#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options
