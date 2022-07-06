import boto3
s3_resource = boto3.client("s3")

#delete single object
s3_resource.delete_object(Bucketv = '',#enterbucketnamehere
      Key = '')#enter file name here

#find all the objects from the bucket
objects = s3_resource.list_objects(Bucket = "")["Contents"]#enterbucketnamehere
len(objects)

#iteration
for object in objects:
    response = s3_resource.delete_object(Bucket = '',#enterbucketnamehere
      Key = object["Key"])
    print(response)