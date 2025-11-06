import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import boto3
from moto import mock_aws
from src.s3_example import create_bucket, list_buckets

@mock_aws
class TestS3Example(unittest.TestCase):
    def setUp(self):
        self.s3 = boto3.client("s3", region_name="us-east-1")

    def test_create_and_list_bucket(self):
        bucket_name = "test-bucket"
        create_bucket(self.s3, bucket_name)
        buckets = list_buckets(self.s3)
        self.assertIn(bucket_name, buckets)

if __name__ == "__main__":
    unittest.main()
