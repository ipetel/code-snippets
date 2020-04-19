/*
let's say you have JSON data and one record looks like this:
  {
    "timestamp": 1579737433091,
    "field_1": 1,
    "field_2": "d346e043-94ae-4365-a64a-902aae332dc6",
    "field_3": "Default_Action",
    "field_4": "REGULAR",
    "field_5": "ALLOW",
    "httpRequest": {
        "clientIp": "123.456.789.0",
        "country": "US",
        "headers": [
            {
              "name": "AAA",
              "value": "1234"
            },
            {
              "name": "BBB",
              "value": "5678"
            },
            {
              "name": "ABA",
              "value": "987"
            }
        ],
  }

and we want to:
  1) filter only records that have 'httpRequest.headers.name'=='AAA'
  2) filter only records that have 'httpRequest.headers.name' like 'A%'
  3) select the 'httpRequest.headers.name' and 'httpRequest.headers.value'
 
 solution based on: https://stackoverflow.com/questions/50766928/presto-array-contains-an-element-that-likes-some-pattern
*/

# 1) filter only records that have 'httpRequest.headers.name'=='AAA'
  SELECT *
  FROM <TABLE-NAME>
  where cardinality(filter(httpRequest.headers, x -> x.name ='AAA')) > 0
  limit 10
  
  # 2) filter only records that have 'httpRequest.headers.name' like 'A%'
  SELECT *
  FROM <TABLE-NAME>
  where cardinality(filter(httpRequest.headers, x -> x.name like 'A%')) > 0
  limit 10
  
  # 3) select the 'httpRequest.headers.name' and 'httpRequest.headers.value'
  # key array in Presto start from 1 (not 0), in the select we assume there is only one field name with 'AAA' value
  SELECT filter(httpRequest.headers, x -> lower(x.name) ='AAA')[1].name name,
         filter(httpRequest.headers, x -> lower(x.name) ='AAA')[1].value value
  FROM <TABLE-NAME>
  limit 10
