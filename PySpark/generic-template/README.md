# AWS Glue Generic Template

This is a generic template for creating Glue Job in PySpark using a Config file

the approach is to use 'DynamicFrames' to read from and write into S3 bucket, and to use 'DataFrame' to preform all the transformations    

### DynamicFrame vs DataFrame in AWS Glue

Note the difference between DynamicFrame and DataFrame. 
DataFrame is Spark native table like structure. 
DynamicFrame class is an attempt from AWS to address limitations of the DataFrame.

DynamicFrames might be handy to read and write data. 
Often the data processing is more efficient with standard PySpark functions.

### Based on
- [mikaelahonen-solita | aws-glue-tutorial](https://github.com/mikaelahonen-solita/aws-glue-tutorial)
- [avensolutions | cdc-in-aws-glue](https://github.com/avensolutions/cdc-in-aws-glue)
