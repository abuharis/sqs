#!/usr/bin/python3

import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='eu-west-1')

queue_url = 'SQS_URL'

# Receive message from SQS queue
response = sqs.receive_message(
            QueueUrl=queue_url,
                AttributeNames=[
                            'SentTimestamp'
                                ],
                    MaxNumberOfMessages=1,
                        MessageAttributeNames=[
                                    'All'
                                        ],
                            VisibilityTimeout=0,
                                WaitTimeSeconds=0
                                )

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

print (message)
