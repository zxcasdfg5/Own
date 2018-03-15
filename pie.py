import boto3
import pprint
from pprint import pprint

s3 = boto3.resource('s3')
print(s3.buckets.all())

for bucket in s3.buckets.all():
    print(bucket.name)  #bucket names


ec2 = boto3.resource('ec2')
print("/nEC2 Instances")
for ins in ec2.instances.all():
    pprint(dir(ins))
    
print("/nEC2 Instances (id, state)")
for ins in ec2.instances.all():
    print(ins.id, ins.state)

"""
if __name__ == "__main__":
    fileName='test.jpg'
    bucket='cap-1'
    
    client=boto3.client('rekognition','ap-northeast-2')

    response = client.detect_labels(Image={'S3Object':{'Bucket':"cap-1",'Name':"test.jpg"}})

    print('Detected labels for ' + "test.jpg")    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
"""