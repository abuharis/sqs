#!/usr/bin/python3

import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='eu-west-1')

queue_url = ''

# Send message to SQS queue
response = sqs.send_message(
            QueueUrl=queue_url,
                MessageGroupId="1",
                    MessageAttributes={
                                'Title': {
                                                'DataType': 'String',
                                                            'StringValue': 'The Whistler'
                                                                    },
                                        'Author': {
                                                        'DataType': 'String',
                                                                    'StringValue': 'John Grisham'
                                                                            },
                                                'WeeksOn': {
                                                                'DataType': 'Number',
                                                                            'StringValue': '6'
                                                                                    }
                                                    },
                        MessageBody=(
                                    'Information about current NY Times fiction bestseller for '
                                            'week of 12/11/2016.add'
                                                )
                        )

print(response['MessageId'])
