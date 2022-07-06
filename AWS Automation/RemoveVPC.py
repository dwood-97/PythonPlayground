import boto3
client = boto3.client("ec2")
client.delete_vpc(
      VpcId = 'vpc-03cabc6a58d44ed67'
      )

print(response)