# Mongo Useful Queries

### Update a field in embedded document (array) by conditional statement
  Assumptions:
  - Collection name: col_1
  - document example
    - {
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

Mongo Shell Command:

- `
db.col_1.updateMany(
  {"metadata.category":"BB"},
  {$set:{"metadata.$[e].value": 1 }},
  { arrayFilters: [ {"e.value":{$gt:0}} ], multi: true }
);
`

Result:

- {
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
      "value": 1
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
<br /><br /><br /><br /><br /><br />



### Update - Pull element from embedded document (array) by conditional statement

  Assumptions:
  - Collection name: col_1
  - document example
    - {
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

Mongo Shell Command:

- `
db.col_1.updateMany(
  {"metadata.category":"BB"},
  {$set:{"metadata.$[e].value": 1 }},
  { arrayFilters: [ {"e.value":{$gt:0}} ], multi: true }
);
`

