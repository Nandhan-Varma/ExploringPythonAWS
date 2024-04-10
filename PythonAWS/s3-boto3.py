import boto3 
client = boto3.client('s3')

#Creating S3 Bucket 
response = client.create_bucket(ACL='private', Bucket='test-bucket-86884589895225', CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})
print(response)


#Uploading File Into S3
bucket = 'test-bucket-86884589895225'
file1 = "F:/ideal_wfh_setup.jpg"
key_name = 'Sample-Image.jpg'

uploadFile1Response = client.upload_file(file1,bucket,key_name)
print(uploadFile1Response)

file2 = "F:/sample.txt"
key_name2 = 'textfile.txt'

uploadFile1Response = client.upload_file(file2, bucket, key_name2)
print(uploadFile1Response)


#Deleting Object 
response = client.delete_object(
Bucket=bucket,
Key='textfile.txt'
)
print(response)

#Listing All Objects in S3 

listOfObjects = client.list_objects(Bucket=bucket)
print(listOfObjects)

#Listing All Buckets in S3
listOfBuckets = client.list_buckets()
print(listOfBuckets)