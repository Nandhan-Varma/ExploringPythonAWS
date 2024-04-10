import boto3
#Creating a new EC2 instance in Mumbai Region

client = boto3.client('ec2')
response = client.run_instances(ImageId='ami-09298640a92b2d12c', InstanceType='t2.micro',
                                MaxCount=1, MinCount=1, SubnetId='subnet-0c54e14a09a804a9e')

print(response)

for info in response['Instances']:
    print(info['InstanceId'])

# Instance Id Generated - i-03d49fb7707bb0b8a

#Starting Instance 
startResponse = client.start_instances(InstanceIds=['i-03d49fb7707bb0b8a'])

print(startResponse)


#Stopping Instance 

stopResponse = client.stop_instances(InstanceIds=['i-03d49fb7707bb0b8a'])
print(stopResponse)

#Terminating Instance 

terminateResponse = client.terminate_instances(
    InstanceIds=['i-03d49fb7707bb0b8a'])

print(terminateResponse)
