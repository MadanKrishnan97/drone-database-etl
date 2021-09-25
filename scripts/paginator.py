import boto3


s3client = boto3.client('s3')
paginator = s3client.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket='part1-test1')

for bucket in page_iterator:
    print(bucket['Contents'])
    for file in bucket['Contents']:
        print(file['Key'])
        try:
            metadata = s3client.head_object(Bucket='part1-test1', Key=file['Key'])
            print(metadata)
        except:
            print("Failed {}".format(file['Key']))
