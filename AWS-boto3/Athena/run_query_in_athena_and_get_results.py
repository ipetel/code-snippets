import boto3

# functions

def get_aws_client(client_name):
    return session.client(client_name)

def run_query_and_get_results_athena(athena_client,query_string,db,output_location):
    query_id = athena_client.start_query_execution(
                    QueryString=query_string,
                    QueryExecutionContext={'Database': db},
                    ResultConfiguration={'OutputLocation': output_location},
                    WorkGroup='primary'
                )['QueryExecutionId']

    query_status = None
    while query_status == 'QUEUED' or query_status == 'RUNNING' or query_status is None:
        query_status = athena_client.get_query_execution(QueryExecutionId=query_id)['QueryExecution']['Status']['State']
        if query_status == 'FAILED' or query_status == 'CANCELLED':
            raise Exception('Athena query with the string "{}" failed or was cancelled'.format(query_string))
            sleep(0.5)
    results_paginator = athena_client.get_paginator('get_query_results')
    results_iter = results_paginator.paginate(
        QueryExecutionId=query_id,
        PaginationConfig={'PageSize': 1000}
    )
    results = []
    column_names = None
    for results_page in results_iter:
        for row in results_page['ResultSet']['Rows']:
           column_values = [col.get('VarCharValue', None) for col in row['Data']]
           if not column_names:
               column_names = column_values
           else:
               results.append(dict(zip(column_names, column_values)))
    print(f'query return {len(results)} items')
    return results

  
# init  
session = boto3.Session(profile_name=<PROFILE>)
aws_athena_client = get_aws_client("athena")

# main

query = '''
         SELECT *
         FROM "<TABLE-IN-GLUE-CATALOG>"
         WHERE name = 'ABC'
         '''

data = run_query_and_get_results_athena(aws_athena_client,query)
