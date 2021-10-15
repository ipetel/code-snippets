# Useful Queries

- db.getSiblingDB("DB").collection.explain("executionStats").aggregate();
- db.getSiblingDB("DB").collection.explain().find();
- db.getSiblingDB("DB").collection.deleteMany({})
<br/><br/><br/><br/><br/>

# compare two fields of same document
```json
  {"$match":{
        "$expr": {
          "$ne"/"$eq": [
            "$field_1",
            "$field_2"
          ]
        }
      }
    }
   }
```
<br/><br/><br/><br/><br/>

# project only one value of array
 Assumptions:
 - Collection name: col_1
 - document example
    - ```json
      {
        "name": "abc1",
        "metadata": [
          {
            "name": "A",
            "category": "AA",
            "value": 0
          },
          {
            "name": "B",
            "category": "BB",
            "value": 3
          },
          {
            "name": "C",
            "category": "BB",
            "value": 1
          },
          {
            "name": "D",
            "category": "CC",
            "value": 5
          }
        ]
      }
      ``` 

Project Command:
```json
{
  "$project": {
    "NEW_FIELD_PROJECT_NAME": {
      "$ifNull": [
        {
          "$arrayElemAt": [
            {
              "$map": {
                "input": {
                  "$filter": {
                    "input": "$metadata",
                    "as": "v",
                    "cond": {"$eq": ["$$v.category","CC"]}
                  }
                },
                "as": "v",
                "in": "$$v.value"
              }
            },
            0
          ]
        },
        null
      ]
    }
  }
}
``` 

Result: 
- ```json
  {
    "NEW_FIELD_PROJECT_NAME": 5
  }
  ``` 
