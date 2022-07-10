import boto3

client = boto3.client('ec2')

response = client.run_instances(ImageId = 'ami-0742b4e673072066f',
                       InstanceType = 't2.micro',
                       MinCount = 2,
                       MaxCount = 2,
                       KeyName = 'CustomVPC',
                       TagSpecifications = [
                           {
                               'ResourceType': 'instance',
                               'Tags': [{'Key': 'Test1','Value': 'Test1pair'},
                                        {'Key': 'Test2','Value': 'Test2pair'}]
                           },
                       ],
                       )
for i in resonse['Instances']:
print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))