import boto3
import os
import psutil
import time

def print_s3_select_results(bucket, key):
    s3 = boto3.client('s3')

    # S3 Select parameters
    s3_select_params = {
        'Bucket': bucket,
        'Key': key,
        'ExpressionType': 'SQL',
        'Expression': "SELECT * FROM s3object s WHERE CAST(s.\"id\" AS INT) >= 68000000 AND CAST(s.\"id\" AS INT) <= 78000000",
        'InputSerialization': {
            'CSV': {
                'FileHeaderInfo': 'USE',
                'RecordDelimiter': '\n',
                'FieldDelimiter': ',',
            }
        },
        'OutputSerialization': {
            'CSV': {}
        }
    }
    result = s3.select_object_content(**s3_select_params)

    # Print the results
    total = 0
    for event in result['Payload']:
        if 'Records' in event:
            payload = event['Records']['Payload'].decode('utf-8')
            #print(payload)
            total += payload.count('\n')
    print(f"Total retrieved: {total}")

process = psutil.Process(os.getpid())
mem_start = process.memory_info().rss

bucket = 'tfg-upload-2023-05-10'
key = 'large-data-file.csv'
#key = 'small-data-file.csv'

print_s3_select_results(bucket, key)
mem_end = process.memory_info().rss

print(f"Peak memory usage: {(mem_end - mem_start) / (1024 * 1024)} MB")
