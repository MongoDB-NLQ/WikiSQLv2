# WikiSQLv2

Patched and improved version of the original large crowd-sourced dataset for developing natural language interfaces for relational databases, [WikiSQL](https://github.com/salesforce/WikiSQL).

## 📂 Content

Inside the `dataset` folder, you will find files in `.jsonl`, `.sql`, and `.txt` formats.

The dataset is split into three partitions:

- **dev** — for validating a model  
- **test** — for testing a model  
- **train** — for training a model  

### Jsonl files categories

For each partition, the main folder contains:

- **`{partition}_tables.jsonl`** — table data (one table per line), including header names, data types, and rows.  
- **`{partition}.jsonl`** — natural language queries, corresponding SQL queries, and the table ID each query refers to.  
- **`{partition}_results.jsonl`** — results from `{partition}.jsonl` queries, including both query output and an example of a correct SQL query.  

### Database Creation

The dataset also includes the `database_creation_sql` folder, containing SQL scripts (`.sql` and `.txt` formats, one query per line) to:

1. Create tables for each partition  
2. Populate them with corresponding data


## Files formats
### `{partition}_tables.jsonl`
```
{
  "header": [
    "Player",
    "No.",
    "Nationality",
    "Position",
    "Years in Toronto",
    "School/Club Team"
  ],
  "page_title": "Toronto Raptors all-time roster",
  "types": [
    "text",
    "text",
    "text",
    "text",
    "text",
    "text"
  ],
  "id": "1-10015132-11",
  "section_title": "L",
  "caption": "L",
  "rows": [
    ["Antonio Lang", "21", "United States", "Guard-Forward", "1999-2000", "Duke"],
    ["Voshon Lenard", "2", "United States", "Guard", "2002-03", "Minnesota"],
    ["Martin Lewis", "32, 44", "United States", "Guard-Forward", "1996-97", "Butler CC (KS)"],
    ["Brad Lohaus", "33", "United States", "Forward-Center", "1996", "Iowa"],
    ["Art Long", "42", "United States", "Forward-Center", "2002-03", "Cincinnati"],
    ["John Long", "25", "United States", "Guard", "1996-97", "Detroit"],
    ["Kyle Lowry", "3", "United States", "Guard", "2012-Present", "Villanova"]
  ],
  "name": "table_10015132_11"
}
```

### `{partition}.jsonl`
```
{
  "phase": 1,
  "table_id": "1-10015132-11",
  "question": "What player played Guard for toronto in 1996-97?",
  "sql": {
    "sel": "Player",
    "conds": [
      ["Position", "=", "Guard"],
      ["Years in Toronto", "=", "1996-97"]
    ],
    "agg": ""
  },
  "question_id": 5
}
```


### `{partition}_results.jsonl`
```
{
  "question_id": 5,
  "table_id": "1-10015132-11",
  "query": "SELECT \"Player\" FROM \"1-10015132-11\" WHERE \"Position\" = 'Guard' AND \"Years in Toronto\" = '1996-97';",
  "result": [
    ["John Long"]
  ]
}
```


## Changes to original dataset
