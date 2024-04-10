import boto3
connection = boto3.client('rds', aws_access_key_id='AKIAVKXOYX3RHE3R7JM5',
                          aws_secret_access_key='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', region_name='ap-south-1')


response = connection.create_db_instance(
    AllocatedStorage=10,
    DBName="test",
    DBInstanceIdentifier="my-first-rds-instance",
    DBInstanceClass="db.t3.micro",
    Engine="mysql",
    MasterUsername="root",
    MasterUserPassword="Nandhan1234",
    Port=3306
)

print(response)
