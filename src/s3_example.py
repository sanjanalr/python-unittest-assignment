import boto3

def create_bucket(s3_client, bucket_name):
    """Creates an S3 bucket."""
    s3_client.create_bucket(Bucket=bucket_name)

def list_buckets(s3_client):
    """Lists all S3 buckets."""
    response = s3_client.list_buckets()
    return [bucket["Name"] for bucket in response["Buckets"]]
