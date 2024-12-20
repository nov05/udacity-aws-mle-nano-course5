import boto3
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
print('🟢 Loading Lambda function...')

def lambda_handler(event, context):
    print('👉 Context:', context)
    print('👉 EventType:', type(event))
    runtime = boto3.Session().client('sagemaker-runtime')
    response = runtime.invoke_endpoint(
        EndpointName=event['endpoint_name'],
        ContentType="application/json",
        Accept='application/json',
        Body=event['request_dict']
    )
    response = json.loads(response['Body'].read().decode())  ## a list of shape (1, 33)
    body = [max(range(len(row)), key=row.__getitem__) for row in response] ## argmax of 2D list, np.argmax(response, 1)
    return {
        'statusCode': 200,
        'headers': { 
            'Content-Type': 'text/plain', 
            'Access-Control-Allow-Origin': '*' 
        },
        'bodyType': str(type(body)),
        'body': json.dumps(body),
        'context': str(context),
    }


'''
input payload:
{
  "endpoint_name": "p4-dog-breed-classification",
  "request_dict": "{\"url\": \"https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/20113314/Carolina-Dog-standing-outdoors.jpg\"}"
}
output example:
[56]
'''