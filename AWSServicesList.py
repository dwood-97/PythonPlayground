#   If you are here from LinkedIn be sure to follow along as I continue this journey with Python!

#   Today we will be going over how to create, edit, and print a list.
#   For this example we will be using AWS services as our topic!

#   The objective of this assignment can be found below.

#1. Create a list of services using Python. IE: S3, Lambda, EC2, etc
#2. The list should be empty initially.
#3. Populate the list using append or insert.
#4. Print the list and the length of the list.
#5. Remove two specific services from the list by name or by index.
#6. Print the new list and the new length of the list.

#   To do this lets start by adding an empty Services list.
Services = []

#   Now lets add in our services
Services += ['Cloud9', 'EC2', 'S3', 'CloudTrail', 'Lambda', 'CloudFormation', 'API Gateway', 'VPC', 'ECS', 'CodeBuild', 'CodeDeploy']

#   Now we can print the list and the length of the list.
Length = "Length = "
ListLength = len(Services)
print(Services)
print(Length, ListLength)

#   Now that we have our list, lets remove two items from the list and run it again.
Services.remove('CloudTrail')
Services.remove('Cloud9')
Length = "Length = "
ListLength = len(Services)
print(Services)
print(Length, ListLength)

#   There we go, task complete! Now we can make a list, add/remove items from it, and print it!