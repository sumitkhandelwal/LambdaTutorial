import json
import csv
import boto3

def lambda_handler(event, context):
    # TODO implement
    region = 'us-east-2'
    record_list = []
    try:
        dynamodb = boto3.client('dynamodb', region_name = region)
        s3 = boto3.client('s3')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        print ("Bucket :", bucket)
        print ("Key :", key)
        
        csv_file = s3.get_object(Bucket = bucket, Key = key)
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        
        csv_reader = csv.reader(record_list, delimiter = ',', quotechar='"')
        
        for row in csv_reader:
            employeeId = row[0]
            userName = row[1]
            employeeName = row[2]
            employeeSalary = row[3]
            
            print("Employee Id :", employeeId, "User name :", userName, "Employee Name :",employeeName, "Salary :", employeeSalary)
            
        
        
            add_to_db = dynamodb.put_item(
                TableName = 'userdetails',
                Item = {
                   'employeeId' : {'N' : str(employeeId)}, 
                   'userName' : {'S' : str(userName)},
                   'employeeName' : {'S' : str(employeeName)},
                   'employeeSalary' : {'S' : str(employeeSalary)},
                })
            
        print("Sucessfully Add record to DynamoDB")
        
    except Exception as e:
        print("Error", str(e))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Sucessful')
    }


import json
import csv
import boto3

def lambda_handler(event, context):
    # TODO implement
    region = 'us-east-2'
    record_list = []
    
    try:
        s3 = boto3.client('s3')
        dynamodb = boto3.client('dynamodb', region_name = region)
        bucket = 'my-training-bucket-hsbcdemo'
        Response = s3.list_objects_v2(Bucket=bucket)
        Files_ListS = Response.get('Contents')
        csv_objects = [f for f in Files_ListS if f['Key'].endswith('.csv')]
        key = max(csv_objects, key=lambda x: x['LastModified'])['Key']
        
        print("Bucket :", bucket)
        print("Key :", key)
        
        csv_file = s3.get_object(Bucket = bucket, Key = key)
        
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        csv_reader = csv.reader(record_list, delimiter = ',', quotechar = '"')
        
        for row in csv_reader:
            employeeID = row[0]
            userName = row[1]
            employeeName = row[2]
            employeeSalary = row[3]
            
            print("Employee ID :", employeeID)
            print("User Code :", userName)
            print("Employee Name :", employeeName)
            print("Employee Salary :", employeeSalary)
            
            add_to_db = dynamodb.put_item(
                TableName = 'employeeRecord',
                Item = {
                    'employeeId' : {'N' : str(employeeID)},
                    'userName' : {'S' : str(userName)},
                    'employeeName' : {'S' : str(employeeName)},
                    'employeeSalary' : {'S' : str(employeeSalary)}
                })
        print("Data Write Sucessfully.")
            
    except Exception as e:
        print("Error", str(e))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Sucess')
    }
