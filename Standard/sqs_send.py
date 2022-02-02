#!/usr/bin/python3

import boto3
import os

# Create SQS client
sqs = boto3.client('sqs', region_name='eu-west-1')

queue_url = os.environ.get('SQS_URL')

# Send message to SQS queue
response = sqs.send_message(
            QueueUrl=queue_url,
                DelaySeconds=10,
                    MessageAttributes={
                                'Title': {
                                                'DataType': 'String',
                                                            'StringValue': 'The Standard Queue'
                                                                    },
                                        'Author': {
                                                        'DataType': 'String',
                                                                    'StringValue': 'Abuharis Salih'
                                                                            },
                                                    },
                        MessageBody=(
                                    'Hello from the Standard Queue'
                                                )
                        )

print(response['MessageId'])
