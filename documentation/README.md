# Project documentation

Use this directory to store documentation related to your project:

1. Project statement.

  The goal of this project is to develop a data ETL pipeline using Python on AWS to organize images taken by a drone. Participants will receive a set of images, and tag information, and the goal is to develop a database that allows others to query images by date, tag and location. The team will focus on building an MVP (Minimum Viable Product - a product with just enough features to be usable) in the hackathon.

  Using cloud is a nice way to ensure that the MVP built during the hackathon can be developed further as required and allows easy scalability (store TBs worth of images) that is important to the data owners.

  This project would be done using AWS cloud services. Python will be used for scripting purposes as required. The data will be stored using S3 and the metadata will be stored using DynamoDB. S3 is an industry standard way of storing data on AWS, and DynamoDB is a NoSQL database on AWS. Boto3 is the Python library that we will use to interact with the AWS services using Python.

2. Write ups your team developed.

Installs needed for this project:
```
pip install Pillow
pip install pyspark
pip install exif
pip install defusedxml  
  ```
  
  Library packages used in this project:
  ```
import PIL as pil
from PIL import Image, JpegImagePlugin
from PIL.ExifTags import TAGS, GPSTAGS
import exif
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import pyspark.ml
import pyspark.mllib
import numpy as np
import json
import os
import pandas as pd
```

The functions we developed to crawl through the images to extract the metadata into a JSON file format:
```
def extract_metadata(path_to_img: str) -> dict:
    """
    Returns dictionary with metadata from image
    --------------------------------------------
    Input: path to the image file (str)
    Output: dictionary with metadata
    """
    img_metadata = {}
    gpsinfo = {}
    image = Image.open(path_to_img)
    exif_data = image.getexif()

    # Get general data
    img_metadata['filename'] = image.filename
    img_metadata['colorspace'] = image.mode
    img_metadata['imgwidth'] = image.width
    img_metadata['imgheight'] = image.height

    # Get exif_data
    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        metadata = exif_data.get(tag_id)
        if isinstance(metadata, bytes):
            metadata = metadata.decode()
        img_metadata[f'exif_{tag}'] = metadata

    # Get xmp data
    image_jpeg = JpegImagePlugin.JpegImageFile(path_to_img)
    image_jpeg_data = image_jpeg.getxmp()

    for tag_, metadata_ in image_jpeg_data['xmpmeta']['RDF']['Description'].items():
        img_metadata[f'xmp_{tag_}'] = metadata_

    for t in img_metadata.keys():
        if isinstance(img_metadata[t], str):
            img_metadata[t] = img_metadata[t].replace('\x00', '')

    return img_metadata
 

# Extract more metadata parameters (might only need a few of the ones that's extracted) 
def extract_more(filepath):
  with open(filepath, 'rb') as image_file:
    image_file = exif.Image(image_file)

  needed_params = image_file.get_all()
  return needed_params

# Returns more metadata on geolocation in dict format
def extract_geolocation(file_path):
  gpsinfo = {}
  image = Image.open(file_path)
  info = image.getexif()
  for key_tag, value in info.items():
      decoded = TAGS.get(key_tag, key_tag)
      gpsinfo[decoded] = value

  geolocation = {}
  for key in gpsinfo['GPSInfo'].keys():
    decode = GPSTAGS.get(key, key)
    geolocation[decode] = gpsinfo['GPSInfo'][key]

  return geolocation


def clean_metadata(metadata_dictionary):
    """
    """
    clean_metadata = {}

    filename_args = metadata_dictionary['filename'].split('/')
    clean_metadata['stage'] = filename_args[-3].lower()
    clean_metadata['imgname'] = filename_args[-1]
    clean_metadata['imglocation'] = '/'.join(filename_args[-3:])
    clean_metadata['format'] = filename_args[-1][-3:]

    data_to_keep = ['imgwidth', 'imgheight', 'colorspace',
                    'exif_DateTime', 'exif_ImageDescription',
                    'xmp_Make', 'xmp_Model',
                    'xmp_GpsLatitude', 'xmp_GpsLongtitude']

    new_labels = ['imgwidth', 'imgheight', 'colorspace',
                  'datetime', 'devicelocation',
                  'make', 'model',
                  'latitude', 'longitude']


    for i in range(len(data_to_keep)):
        new_key = new_labels[i]
        old_key = data_to_keep[i]
        clean_metadata[new_key] = metadata_dictionary[old_key]

    return clean_metadata


def metadata_dict_to_json(clean_metadata_dict):
    """
    Returns structured JSON from input dictionary
    ---------------------------------------------
    input: dictionary of file metadata
    output: clean metadata json
    """
    clean_metadata_json = json.dumps(clean_metadata_dict)

    return clean_metadata_json


if __name__ == "__main__":

    example_img_ruiz = 'C:/Users/owner/Documents/Data Science/Datasets/100_0006_0001 (2).JPG'

    example_img = 'C:/Users/G-Unit/Desktop/Arisa/VDJ2021/' \
                  'drone-database-etl-copy/data/Part1/Images/100_0006_0001 (2).JPG'

    print(os.path.getsize(example_img))
    metadata_dict = extract_metadata(example_img)
```

3. Diagrams your team designed.


4. Documentation on the process you followed.


