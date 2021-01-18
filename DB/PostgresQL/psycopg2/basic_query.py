import psycopg2
from functools import wraps
import logging


# ___ logging config
LOG_LEVEL = logging.DEBUG
logging.basicConfig(level=LOG_LEVEL, format='### %(levelname)s ### - line: %(lineno)s, function: %(funcName)s(), msg: %(message)s')

# ___ Decorators

def try_except(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        try:
            response = orig_func(*args, **kwargs)
            logging.info(f'{orig_func.__name__}() function operation was completed successfully')
            return response
        except Exception as err:
            logging.error(f'{err}')
    return wrapper

# ___ Functions

@try_except
def get_connection_to_db(rds_conn_details):
    print(rds_conn_details,type(rds_conn_details))
    return psycopg2.connect(
        dbname=rds_conn_details["dbname"], 
        user=rds_conn_details["username"], 
        password=rds_conn_details["password"], 
        host=rds_conn_details["host"], 
        port=rds_conn_details["port"]
    )

@try_except
def send_query_to_db(query,conn):
    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    # Execute a query
    cur.execute(query)
    
    # get the data    
    return cur.fetchall()

# ___ Main

if __name__ == "__main__":
  rds_conn_details = {"dbname":"test","username":"test","password":"test","host":"test","port":"1234"}
  conn = get_connection_to_db(rds_conn_details)
  query = "SELECT * FROM table where id >2"
  res = send_delete_query_to_db(query,conn)

  print(res)

