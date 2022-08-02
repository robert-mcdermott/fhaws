import re
import boto3

def get_instances(profile):
    """get_users returns a list of all EC2 instances in the account"""
    session = boto3.Session(profile_name=profile, region_name="us-west-2")
    client = session.client("ec2")
    response = client.describe_instances()

    all_instances = []

    instances = response["Reservations"]

    while "NextToken" in instances:
        instances = client.describe_instances(NextToken=response["NextToken"])
        instances.extend(instances["Reservations"])
    
    for instance in instances:
        all_instances.append(instance)

    return(all_instances)
