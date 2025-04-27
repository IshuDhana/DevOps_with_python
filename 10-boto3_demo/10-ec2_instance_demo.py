import boto3

client = boto3.client('ec2')
response = client.delete_launch_template(
    LaunchTemplateId='i-0339e5b368b7d60e7'
)

'''
response = client.delete_key_pair(
    KeyName='new_pair'
)

print(response)
'''


'''
#terminating ec2 instance
client = boto3.client('ec2')

response = client.terminate_instances(
    InstanceIds=['i-0339e5b368b7d60e7']
)

#stoping ec2 instance
client = boto3.client('ec2')

response = client.stop_instances(
    InstanceIds=['i-0339e5b368b7d60e7']
)

#starting ec2 instance
client = boto3.client('ec2')

response = client.start_instances(
    InstanceIds=['i-0339e5b368b7d60e7']
)

'''
'''Running Ec2 instance 

    response = client.run_instances(
    ImageId = 'ami-0ce8c2b29fcc8a346',
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1,
    KeyName = 'new_pair'
)

print(response)

for instance in response['Instances']:
    print("Instance ID is created : {} Instance Type is : {}". format(instance['InstanceId'], instance['InstanceType']))'''

'''launching boto3 python with terraform
import boto3
aws_management_console = boto3.session.Session(profile_name="terraform-user")'''