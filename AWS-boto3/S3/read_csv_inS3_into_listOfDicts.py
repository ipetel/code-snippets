import boto3, io, csv

s3_client = boto3.resource('s3')

def read_object_from_s3_bucket(s3_obj_key,bucket_name):
    try:    
        source_bucket_resource = s3_client.Bucket(bucket_name)
        content_object = source_bucket_resource.Object(s3_obj_key)
    
        #collected data in the form of bytes array + Decode it in 'utf-8' format
        file_content = content_object.get()['Body'].read().decode('utf-8')
        
        #StringIO object
        f = io.StringIO(file_content)
        
        #read data as CSV to dict stricture
        reader = csv.DictReader(f, ('col_1','col_2','col_3'))
        list_of_dict = [dict(x) for x in reader]
        f.close()
        
        #remove 'None' keys in each of the dicts
        for x in list_of_dict:
            if None in x:
                del x[None]
        
        return list_of_dict
    except ValueError:
        print(f'[### ERROR] - while trying to read from "{s3_obj_key}" file - error message: {ValueError}')
        return None
