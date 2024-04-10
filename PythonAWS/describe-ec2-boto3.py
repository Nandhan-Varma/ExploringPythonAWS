import boto3

client = boto3.client('ec2')

# response = client.run_instances(ImageId='ami-09298640a92b2d12c', InstanceType='t2.micro',
#                                 MaxCount=3, MinCount=1, SubnetId='subnet-0c54e14a09a804a9e')

# print(response)

#Instance id Which are created 
# i-04a6913e8d2ac5d84
# i-0f93a00612e0d66bc
# i-016bb198441b456b1


#Terminating Instance 

# terminateResponse = client.terminate_instances(InstanceIds=['i-0f93a00612e0d66bc'])
# print(terminateResponse)


describeStatus = client.describe_instance_status(
    InstanceIds=['i-04a6913e8d2ac5d84', 'i-0f93a00612e0d66bc', 'i-016bb198441b456b1'])


for response in describeStatus['InstanceStatuses']:
    print("The Info About The Instance With Id {} having state {} with status {}".format(response['InstanceId'],response['InstanceState'],response['InstanceStatus']))
