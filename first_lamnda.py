import json
import boto3
import urllib

s3 = boto3.resource('s3') 
def lambda_handler(event, context):
    # TODO implement
    source_bucket=event['Records'][0]['s3']['bucket']['name']
    key=str(event['Records'][0]['s3']['object']['key'])
    print(source_bucket,key)
    
    copy_source = {
    'Bucket': source_bucket,
    'Key': key
    }
    bucket = s3.Bucket('bucket3gopi')
    bucket.copy(copy_source, key)
    
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }