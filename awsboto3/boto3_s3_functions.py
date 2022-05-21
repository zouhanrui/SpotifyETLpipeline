import boto3
import os

s3_client = boto3.client('s3')


def delete_object(bucket_name, object_name):
    s3_client.delete_object(Bucket=bucket_name, Key=object_name)
    print('Successfully deleted ' + f'{object_name}' + ' from ' + f'{bucket_name}.')


def upload_file(file_path, bucket_name, key=None):
    # get the object name or key
    if key is None:
        key = os.path.basename(file_path)
    s3_client.upload_file(file_path, bucket_name, key)
    print('Successfully uploaded ' + f'{key}' + ' to ' + f'{bucket_name}.')


def list_objects_from_bucket(bucket_name):
    response = s3_client.list_objects(Bucket=bucket_name)
    # print(response.keys())
    objects = []
    if 'Contents' in response.keys():
        for content in response['Contents']:
            objects.append(content['Key'])
    return objects


def list_buckets():
    response = s3_client.list_buckets()
    bucket_names = []
    for bucket in response['Buckets']:
        bucket_names.append(bucket['Name'])
    return bucket_names


def main():

    buckets = list_buckets()
    all_objects_by_bucket = {}
    for bucket in buckets:
        # print(bucket)
        objects = list_objects_from_bucket(bucket)
        all_objects_by_bucket[bucket] = objects
    print(all_objects_by_bucket)
"""
    # Upload the file to bucket
    upload_file('/Users/hanruizou/PycharmProjects/sportifyETLpipeline/data/Drive',
                'python-boto3-test')

    # Delete the file from bucket 
    delete_object(bucket_name='python-boto3-test', object_name='Driver_upload_from_local.csv')
"""



if __name__ == '__main__':
    main()
