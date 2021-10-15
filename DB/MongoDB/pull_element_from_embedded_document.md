# Update - Pull element from embedded document (array) by conditional statement

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

Mongo Shell Command:
- ``` 
  db.col_1.updateMany(
    {"metadata.category":"BB"},
    {"$pull":{"metadata":{"category":"BB"}}},
    { multi: true }
  );
  ```
  
Result: 
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
        "name": "D",
        "category": "CC",
        "value": 5
      }
    ]
  }
  ``` 
