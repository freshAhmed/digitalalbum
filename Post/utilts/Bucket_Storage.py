import boto3
from decouple import config

class Bucket_Storage():
 __aws_access_key=config('CLOUDFLARE_R2_ACCESS_KEY')
 __aws_secret_access_key=config('CLOUDFLARE_R2_SECRET_KEY')
 __endPoint=config('CLOUDFLARE_R2_BUCKET_ENDPOINT')
 __nameservice='s3'
 __BucketName=config('CLOUDFLARE_R2_BUCKET_NAME')


 def __init__(self):
  self.__client=boto3.client(
   service_name=self.__nameservice,
   endpoint_url=self.__endPoint,
   aws_access_key_id=self.__aws_access_key,
   aws_secret_access_key=self.__aws_secret_access_key,
   region_name='auto'
  )
 def get_all(self,Prefix):
   try:
    response=self.__client.list_objects_v2(Bucket=self.__BucketName,Prefix=Prefix)
   except Exception as e :
    raise  e
   return response
 
 def get_object(self,Key):
  try:
   response=self.__client.head_object(Bucket=self.__BucketName,Key=Key)
  except Exception as e:
   raise e
  return response
 
 def delete_object(self,Key):
  try:
   response=self.__client.delete_object(Bucket=self.__BucketName,Key=Key)
  except Exception as e:
   raise e
  return response
  