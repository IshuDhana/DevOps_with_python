import boto3

client= boto3.client('lambda')


response = client.create_function(
    FunctionName='My_first_lambda',
    Runtime='python3.13',
    Role='string',
    Handler='string',
)

