#usr/bin/env python
import click
import boto3

def labels(bucket, name):
	"""This takes an S3 bucket and a image name"""
	
	print(f"This is the bucketname {bucket} !")
	print(f"This is the imagename {name} !")
	rekognition = boto3.client("rekognition")
	response = rekognition.detect_labels(
			Image={
				"S3Object": {
					"Bucket": bucket,
					"Name": name,
				}
			},
		)
	labels = response['Labels']
bucket ="function-bike-rider-ms"
name ="cat.jpg"
results = labels(bucket,name)	
print (results)
	