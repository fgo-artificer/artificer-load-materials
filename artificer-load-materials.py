import boto3
import json

DYNAMODB_TABLE_NAME_MATERIALS = 'artificer-materials'
FILE_NAME = 'materials.json'
S3_BUCKET_NAME_TRANSFORM = 'artificer-transform'

ddb_table = boto3.resource('dynamodb').Table(DYNAMODB_TABLE_NAME_MATERIALS)
s3_bucket_transform = boto3.resource('s3').Bucket(S3_BUCKET_NAME_TRANSFORM)

'''
download_json_from_s3

Download file to local filesystem, open file and return the contents as json
'''
def download_json_from_s3(remote_file_name):
    s3_bucket_transform.download_file(Key=remote_file_name, Filename='/tmp/' + remote_file_name)
    f = open('/tmp/' + remote_file_name, 'r')
    return json.loads(f.readline())

'''
load_materials

Upload json object to DynamoDB
'''
def load_materials(json_obj):
    for each_entry in json_obj['data']:
        ddb_table.put_item(Item=each_entry)

'''
main

Driver function for local execution
'''
def main():
    json_materials = download_json_from_s3(FILE_NAME)
    load_materials(json_materials)

'''
lambda_handler

Driver function for lambda execution
'''
def lambda_handler(event, context):
    main()

main()
