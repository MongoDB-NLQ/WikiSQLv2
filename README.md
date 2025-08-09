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

- **`{partition}.jsonl`** — natural language queries, corresponding SQL queries, and the table ID each query refers to.  
- **`{partition}_tables.jsonl`** — table data (one table per line), including header names, data types, and rows.  
- **`{partition}_results.jsonl`** — results from `{partition}.jsonl` queries, including both query output and an example of a correct SQL query.  

### Database Creation

The dataset also includes the `database_creation_sql` folder, containing SQL scripts (`.sql` and `.txt` formats, one query per line) to:

1. Create tables for each partition  
2. Populate them with corresponding data

