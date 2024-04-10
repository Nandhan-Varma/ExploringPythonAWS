import boto3
connection = boto3.client('rds')


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
