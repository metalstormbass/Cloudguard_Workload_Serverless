import json
import os
import boto3




def lambda_handler(event, context):
    #Parse event
    print (event)
    data = event['data']

    
    # Send message to SNS
    sns_arn = os.environ['SNS_ARN']
    sns_client = boto3.client('sns')
    sns_client.publish(
    TopicArn = sns_arn,
    Subject = 'Check Point Serverless Test',
             Message = "This is the information sent to the Lambda Function: " + data
    )
