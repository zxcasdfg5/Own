import boto3
from pprint import pprint
import helper

client = boto3.client('rekognition')
imgurl = 'https://s3.ap-northeast-2.amazonaws.com/cap-1/test.jpg'
imgbytes = helper.get_image_from_url(imgurl)
rekresp = client.detect_labels(Image={'Bytes': imgbytes},
                                MinConfidence=1)

#pprint(rekresp)
print("Heres's what I see in the image :")
for label in rekresp['Labels']:
    print(label['Name'])