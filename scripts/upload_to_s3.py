# Subtask 2.1 - Parse JSON and upload images/files into S3. Return S3 URI once uploaded.

# local file location: 'C:/Users/G-Unit/Desktop/Arisa/VDJ2021/drone-database-etl-copy/data'
# s3 bucket name: part1-test1


import boto3
from file_crawler import get_file_locations, get_root_structure
from metadata_extraction import extract_metadata, clean_metadata


def download_from_uris(listofuris):
    s3 = boto3.client('s3')

    filenames = []
    objectnames = []

    for uri in listofuris:
        split_uri = uri.split('/')
        filenames.append(split_uri[-1])
        objectnames.append('/'.join(split_uri[-4:]))
        bucketname = split_uri[2]

    for i in range(len(listofuris)):
        s3.download_file(bucketname, objectnames[i], filenames[i])

def uri_to_url(uri_lists):

    for uri in uri_lists:
        split_uri = uri.split('/')
        objectname = '/'.join(split_uri[-4:])
        bucketname = split_uri[2]
        url = f'https://{bucketname}.s3.us-east-2.amazonaws.com/{objectname}'



uris = ['s3://vdjhackathon/dataset/Part1/Images/100_0006_0001 (2).JPG',
        's3://vdjhackathon/dataset/Part1/Images/100_0006_0001 (2).JPG']

download_from_uris(uris)


if __name__ == '__main__':

    # Get file_paths
    root = input('File Location:')
    root_structure = get_root_structure(root)
    img_files, other_files = get_file_locations(root_structure)

    # Get metadata of images
    imgs_metadata = [clean_metadata(extract_metadata(img_file)) for img_file in img_files]
    imgs_locations = [x['imglocation'] for x in imgs_metadata]

    # Instantiate s3
    s3 = boto3.client('s3')

    # s3 bucketname
    s3_bucket = str(input('Your s3 bucket name:'))

    # Storing s3_uri
    s3_uri = []

    # Upload files into s3
    # For each filepath
    for i in range(2):

        file_location = img_files[i]
        file_metadata = imgs_metadata[i]
        file_name = imgs_locations[i]

        for k, v in file_metadata.items():
            file_metadata[k] = str(v)

        s3.upload_file(file_location, s3_bucket, file_name,
                       ExtraArgs={'Metadata': file_metadata})

        uri = f's3://{s3_bucket}/{file_location}'
        s3_uri.append(uri)

    print("Your s3 URIs:")
    for u in s3_uri:
        print(u)