import boto3

client = boto3.client('sqs')

response = client.create_queue(
    QueueName='StandardQueue',
    tags={
        'test1': 'test1pair'
    }
)
print(response)