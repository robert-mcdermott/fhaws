import boto3
from fhaws.sts import role_chain
from fhaws.org import getaccounts


#boot up a session and log into account using default profile
#running aws-configure in fresh termninal is a fast way to set up default profile if you haven't done it before
my_session = boto3.Session(profile_name='default')

#test - print account number
print(boto3.client('sts').get_caller_identity()['Account'])

#test - query S3 buckets residing in parent account
s3_client = boto3.client('s3')
response = s3_client.list_buckets()
for bucket in response['Buckets']:
   print(f'  {bucket["Name"]}')


#test - role chain into child account, can provide either the friendly name or the account # if you know it
child_account = role_chain('default', 'insert role here', 'insert child account here')


#test - grab access keys from role_chain function and use them to access child account's S3 service
s3_client = boto3.client('s3', aws_access_key_id=child_account[0],aws_secret_access_key=child_account[1],aws_session_token=child_account[2])

#test - query S3 and return bucket names
#note that command here is the same as before, but resutls are different b/c we're in the child account vs parent
response = s3_client.list_buckets()
for bucket in response['Buckets']:
   print(f'  {bucket["Name"]}')

