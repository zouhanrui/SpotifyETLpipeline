import os
from typing import Tuple, List, Any

import boto3
import logging
from botocore.exceptions import ClientError



"""
s3_client = boto3.client('s3')
response1 = s3_client.list_buckets()

response2 = s3_client.create_bucket(Bucket='python-boto3-test-create-from-python', CreateBucketConfiguration={'LocationConstraint':'us-west-2'})
print(response1['Buckets'])

for bucket in response1['Buckets']:
    print(bucket['Name'])
"""



def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to an s3 bucket

      :param file_name: File to upload
      :param bucket: Bucket to upload to
      :param object_name: S3 object name. If not specified then file_name is used
      :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
        print(object_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_bucket_content(bucket_name):
    s3_client = boto3.client('s3')
    objects = s3_client.list_objects(Bucket=bucket_name)

    for content in objects['Contents']:
        print(content['Key'])


def list_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    buckets = response['Buckets']
    for bucket in buckets:
        print(bucket['Name'])

def main():
    #upload_file('/Users/hanruizou/PycharmProjects/sportifyETLpipeline/data/Drive', 'python-boto3-test-create-from-python')
    list_bucket_content('python-boto3-test-create-from-python')
    list_buckets()

if __name__ == '__main__':
    main()


