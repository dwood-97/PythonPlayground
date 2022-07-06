import boto3
aws_resource = boto3.resource("s3")
#name the bucket here
bucket = aws_resource.Bucket("")
response = bucket.create(
#add public or private after ACL
    ACL = '',
)

print(response)