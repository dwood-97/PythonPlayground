import boto3
client=boto3.client("ec2")
#How to describe all VPC's in AWS account
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    
#How to describe one VPC based on your VPC ID
x=client.describe_vpcs(VpcIds=["vpc-0ec621e2bf683c5e4", "vpc-0a6ce6202e1be2e87"])
x=client.describe_vpcs
x=client.describe_vpcs(Filters=[
          {
              'Name': 'vpc-id',
              'Values': [
                  "vpc-0ec621e2bf683c5e4", "vpc-0a6ce6202e1be2e87"
                  
              ]
          },
      ])
print(x)