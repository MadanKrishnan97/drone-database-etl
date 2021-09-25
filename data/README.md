# Data directory

It is preferable that you list your data sources in this readme. **Do not store other organization's data in this 
repository unless you made significant changes to it and you are comfortable with others accessing it.**

Data sources selected for the event are public. Check the licenses of these data sources to ensure you give proper 
attribution and indicate what changes you made. 

You can also use this directory to document how you processed the data. 

### Data source:
British Columbia Institute of Technology, Remotely Piloted Aircraft Systems

### Data format:

#### Images
- .JPG format
- metadata extracted from exif and xmp

#### Metadata

All metadata values are str

For Images (filled out if information is extracted):
- `stage` - project stage
- `imagename` - name of the image file
- `imglocation` - location of image file from root folder
- `createdtime` - time of file creation
- `filetype` - file format
- `imgheight` - height in pixels
- `imgwidth` - width in pixels
- `imagearea` 
- `devicemake` - make name of drone
- `devicemodel` - model name of drone
- `colorspace` - color space used (eg RGB)
- `colorprofile`
- `focallength`
- `devicelocation` - filepath to ?
- `alpha`
- `redeye`
- `metering`
- `fnumber`
- `exposure`
- `exposuretime`
- `latitude` - latitude in degrees
- `longitude` - longitude in degrees

Other files:
- `stage`
- `filename`
- `filelocation`
- `createdtime`
- `filetype`