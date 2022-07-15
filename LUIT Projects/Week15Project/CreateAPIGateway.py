import boto3

client = boto3.client('apigateway')
response = client.create_resource(
    restApiId='34242346',
    parentId='9765377854',
    pathPart='/Week15Project'
)
{
    'methodIntegration': {
        'type': 'HTTP'
                }
            }

print(response)
