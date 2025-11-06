import boto3

def create_table(dynamodb_client, table_name):
    """Creates a DynamoDB table."""
    dynamodb_client.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )

def list_tables(dynamodb_client):
    """Lists all DynamoDB tables."""
    response = dynamodb_client.list_tables()
    return response["TableNames"]
