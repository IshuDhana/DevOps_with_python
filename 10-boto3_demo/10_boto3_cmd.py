import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='IshuDhana-demo-boto3-yt-123',
)