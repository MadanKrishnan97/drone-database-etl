# Subtask 1.2 - Extract metadata from images using Pillow, and transform some of them as needed.
# Subtask 1.3 - Define JSON structure and work collaboratively to generate a standard JSON for each file

# TODO 1. Access more metadata 'stage', 'colorprofile', 'focallength', 'alpha',
#                              'redeye', fnumber', 'metering', 'exposure', 'exposuretime'
# TODO 2. Clean dictionary contents
# TODO 3. Add try/except statements

from PIL import Image, JpegImagePlugin
from PIL.ExifTags import TAGS, GPSTAGS
import os
import json


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

### Start of Ruizs Addition
### Requires: !pip install exif
### !pip install defusedxml 

# Extract more metadata parameters (might only need a few of the ones that's extracted) 
def extract_more(filepath):
  with open(filepath, 'rb') as image_file:
    image_file = Image(image_file)

  all_values = image_file.get_all()
  return all_values

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

### End of Ruizs Addition


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

    # Datetime unclear about 'creation'
    # Missing colorprofile, focallength, alpha, redeye, metering, fnumber,
    # exposure, exposuretime

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

    for k, v in metadata_dict.items():
        print(f'{k}:{v}')

    print('======')

    print(metadata_dict_to_json(clean_metadata(metadata_dict)))

### Start of testing space for Ruiz's additional functions
    print('======')

    more_geo = extract_geolocation(example_img_ruiz)
    print(more_geo)

    print('======')
    more_data = extract_more(example_img_ruiz)

### End of Ruiz's test space
