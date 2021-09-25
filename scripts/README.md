# Scripts directory

### 1. file_crawler.py

- contains two functions: `get_root_structure` and `get_file_paths` 
- get_root_structure - gets the file structure of the file path inputted and return a dictionary
- get_file_paths - returns a list of file paths to image files and another list of file paths to non-image files
- see how it works by running: `python file_crawler.py` and typing a file path with image and non-image files

###2. metadata_extraction.py

- contains three functions: `extract_metadata`, `clean_metadata`, and `metadata_dict_to_json`
- extract_metadata - gets a dictionary of metadata from image files (only works with .JPG files)
- clean_metadata - cleans the dictionary output from extract_metadata
- metadata_dict_to_json - translates dictionary into a json
- see how it works by editing the `example_img` string and running `python metadata_extraction.py`

###3. upload_to_s3.py

- takes in a file path and bucket name as input
- this script will upload all image files that exist in the specified file path into the specified s3 bucket
- aws and s3 must be configured before use

###4. flask_app.py

- this script will create a Python API
- when it is running, the user can query for image files taken within a certain range of latitude and longitude
- the url will be: `http://localhost:8080/bcit/drone/data/get/image/longitude/from/min_lon/to/max_lon/latitude/from/min_lat/to/max_lat` where min_lon, max_lon, min_lat, max_lat can be inputted by the user
- the app will query the database for images taken within the specified range and render them as html


## Required sections

### Set up

Tell what we need to install for the scripts to run successfully (i.e. libraries)

### Command line parameters (if applicable) or code snippets demonstrating code usage

    python my_python_script.py parameter1
    
### Script considerations and limitations
