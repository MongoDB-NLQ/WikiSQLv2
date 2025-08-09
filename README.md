# WikiSQLv2

Patched and improved version of the original large crowd-sourced dataset for developing natural language interfaces for relational databases, [WikiSQL](https://github.com/salesforce/WikiSQL).

## Content and format

Inside dataset folder you will find files in jsonl, sql and txt formats.

Dataset is seperated into three partitions:
- dev: Partition for validating a model.
- test: Partition for testing a model.
- train: Partition for training a model.

The main folder includes four types of files in the following format for each partition:
- {partition}.jsonl:
- {partition}_tables.jsonl:
- {partition}_results.jsonl:
- {partition}_results_case_insensitive:

dataset also features database_creation_sql folder where SQL scripts (in sql and txt format - one query per line) are located.
The scrips include queries to create tables for every partition and fill each with corresponding tables.




