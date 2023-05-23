from drinks_api_client import *
import boto3
s3 = boto3.client('s3')

def read_and_upload(file_name, bucket_name):
    # first arg is to read from ......... then write to
    s3.upload_file(file_name, bucket_name, file_name)

def read_data_from(bucket, object):
    pass

def store_restaurant_data(restaurants, bucket):
    pass


