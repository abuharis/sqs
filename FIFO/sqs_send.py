#!/usr/bin/python3

import boto3
import os

# Create SQS client
sqs = boto3.client('sqs', region_name='eu-west-1')

queue_url = os.environ.get('SQS_URL_FIFO')

print (queue_url)

# Send message to SQS queue
response = sqs.send_message(
            QueueUrl=queue_url,
                MessageGroupId="mygroup",
                    MessageAttributes={
                                'Title': {
                                                'DataType': 'String',
                                                            'StringValue': 'SQS TEST'
                                                                    },
                                        'Author': {
                                                        'DataType': 'String',
                                                                    'StringValue': 'Abuharis Salih'
                                                                            },
                                                    },
                        MessageBody=(
                                    'Test message from Abu'
                                                )
                        )

print(response['MessageId'])
