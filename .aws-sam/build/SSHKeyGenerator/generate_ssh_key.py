import boto3
import os
from botocore.exceptions import ClientError
import cfnresponse 

KEY_NAME = "m2m.sourcekey"

def create_key(event, context):
    try:
        # create key
        ec2 = boto3.client("ec2")
        result = ec2.create_key_pair(KeyName=KEY_NAME)
        key = result['KeyMaterial']

        # store key as SSM parameter
        ssm = boto3.client("ssm")
        ssm.put_parameter(Name=KEY_NAME, Type="String", Value=key, Overwrite=True)
        cfnresponse.send(event, context, cfnresponse.SUCCESS)
    except Exception as e:
        print(e)
        cfnresponse.send(event, context, cfnresponse.FAILED)      

def delete_key(event, context):
    try:
        # delete EC2 key
        ec2 = boto3.client("ec2")
        ec2.delete_key_pair(KeyName=KEY_NAME)

        # delete SSM parameter
        ssm = boto3.client("ssm")
        ssm.delete_parameter(Name=KEY_NAME)
        cfnresponse.send(event, context, cfnresponse.SUCCESS)
    except Exception as e:
        print(e)
        cfnresponse.send(event, context, cfnresponse.FAILED)      


def lambda_handler(event, context):
    """ Create EC2 SSH key in current account and store it in SSM Parameter store as m2m.sourcekey """
    print("*** Event ***")
    print(event)

    if event['RequestType'] == 'Update':
        cfnresponse.send(event, context, cfnresponse.SUCCESS)
    elif event['RequestType'] == 'Create':
        create_key(event, context)
    elif event['RequestType'] == 'Delete':
        delete_key(event, context)
    else:
        # just in case
        cfnresponse.send(event, context, cfnresponse.FAILED)
  