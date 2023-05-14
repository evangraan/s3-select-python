# Introduction

This repository explores large CSV file handling on AWS S3

## Generating a large file

In order to test, a simple CSV schema is used:

```
id,name,surname,phone number,category
```

A large number of (78,000,000) entries were then randomly generated, using up to 20 characters per field (see large-file-generator.py). The records in the file are numerically ordered with ids from 1 to 78,000,000

The output file is `large-data-file.csv`. An arbitrary subset of this file can be taken to create smaller data files, e.g.:

`head -n 10000 large-data-file.csv > small-data-file.csv`

## S3

This file can be uploaded to an AWS S3 bucket for testing.

## Pandas access

The file can be accessed using pandas as in the `panda_select.py` example.

The challenges how-ever are that pandas iterates each line in the file and as such the full S3 object is downloaded when processing it. This takes a long time and uses a lot of data.

## S3 select

S3 provides a method to select a subset from an S3 object using a SQL query. See `s3_select.py` for an example.

In this case, only the records required are accessed and transferred to the program.

This makes S3 select ideal for ETL jobs.

## Performance

Running the S3 select program on a Macbook Pro 15" 2018 yields the following performance.

### 1 million records retrieved

Total retrieved: 1000001
Peak memory usage: 14.515625 MB
python3 s3_select.py 0.87s user 0.98s system 2% cpu 1:03.97 total
Records per second: 15625

### 10 million records retrieved

Total retrieved: 10000001
Peak memory usage: 12.11328125 MB
python3 s3_select.py 5.17s user 5.50s system 5% cpu 3:17.65 total
Records per second: 50505

The implication is that 8 parallel lambdas could do ETL on these records in 3.5 minutes total, depending on the lambda processor type and the requirements of the translation.
