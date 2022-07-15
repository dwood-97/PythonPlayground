import boto3
ec2_client = boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone = 'us-east-2c',
      Encrypted = True,
      Size = 12,
      SnapshotId = 'string',
      VolumeType = 'gp2')
      
print(ec2_client)