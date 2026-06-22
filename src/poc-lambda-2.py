import boto3
import json

client = boto3.client('sns')

def lambda_handler(event, context):
    for record in event["Records"]:
        if record['eventName'] == 'INSERT':
            new_record = record['dynamodb']['NewImage']
            
            response = client.publish(
                TargetArn='<YOUR_SNS_TOPIC_ARN_HERE>',
                Message=json.dumps({'default': json.dumps(new_record)}),
                MessageStructure='json'
            )