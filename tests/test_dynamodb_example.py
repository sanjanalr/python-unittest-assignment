import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import boto3
from moto import mock_aws
from src.dynamodb_example import create_table, list_tables

@mock_aws
class TestDynamoDBExample(unittest.TestCase):
    def setUp(self):
        self.dynamodb = boto3.client("dynamodb", region_name="us-east-1")

    def test_create_and_list_table(self):
        table_name = "test-table"
        create_table(self.dynamodb, table_name)
        tables = list_tables(self.dynamodb)
        self.assertIn(table_name, tables)

if __name__ == "__main__":
    unittest.main()
