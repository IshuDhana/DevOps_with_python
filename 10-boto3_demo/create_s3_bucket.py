import boto3


#s3_client = boto3.client('s3')

#create s3 bucket using boto3 command
#s3_client.create_bucket(Bucket="ishu-dhana-bucket-demo3", CreateBucketConfiguration = {'LocationConstraint':'eu-west-1'})

#list buckets using boto3 command
#response = s3_client.list_buckets()
#print(response)

#put objects into bucket using boto3 -  write operation
#data = "ishu"
#response = s3_client.put_object(Body=data, Bucket='ishu-dhana-bucket-demo3', Key = 'new_file')
#print(response)

#get objects into bucket using boto3 - read operation
#response = s3_client.get_object(Bucket ='ishu-dhana-bucket-demo3', Key = 'new_file' )
#data = response['Body'].read()
#print(data)

#upload file from local machine into aws using noto3 python
#response = s3_client.upload_file(r'c:\Users\Soundharya\Documents\code\DevOps_with_python\07-file_operations\demofile.txt', 'ishu-dhana-bucket-demo', 'demofile.txt')
#print(response)

#download file from s3 bucket
#response = s3_client.download_file('ishu-dhana-bucket-demo3','new_file',r'C:\Users\Soundharya\Documents\new_file')
#print(response)

#copy data from one s3 bucket to another s3 bucket
#s3 = boto3.resource('s3')
#copy_source = {
 #   'Bucket':'ishu-dhana-bucket-demo3',
  #  'Key':'new_file'
#}
#bucket =s3.Bucket('ishu-dhana-bucket-demo2')
#bucket.copy(copy_source,'copied-data/new_file')

'''list object from s3 bucket
client = boto3.client('s3')
response = client.list_objects_v2(
    Bucket = 'ishu-dhana-bucket-demo2',
    Prefix = 'copied_data/'
)

for key in (response):
    print(key)

client = boto3.client('s3')
response = client.delete_object(
     Bucket = 'ishu-dhana-bucket-demo',
     Key = 'new_file'
)
print(response)'''

client = boto3.client('s3')
response = client.delete_bucket(
    Bucket='ishu-dhana-bucket-demo'
)
print(response)

