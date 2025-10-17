import boto3

# Retrieve the list of existing buckets using the 'practice' profile
session = boto3.Session(profile_name='practice')
s3 = session.client('s3')
iam = session.client('iam')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

iam.delete_user(
    UserName='IAM_USER_NAME'
)

# # Create IAM client
# iam = session.client('iam')

# # Create user
# response = iam.create_user(
#     UserName='IAM_USER_NAME'
# )

# print(response)

# List users with the pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)

