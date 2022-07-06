import boto3
import os
import glob

#How to upload a single file
s3_resource = boto3.client("s3")
s3_resource.upload_file(
Filename = "",
Bucket = "",
Key = "")

    
#For multi-file uploads
cwd = os.getcwd()
cwd = cwd + "/"#Either change your CWD and just enter "/" or enter in the CWD here
files = glob.glob(cwd + "/*.py")

for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
    Filename =  file,
    Bucket = "dylanboto3bucket",
    Key = file.split("/")[-2]#[]<----- First run code to find position of file you want to upload then run with correct positioning in the brackets
    )
    
print(cwd)
print(files)