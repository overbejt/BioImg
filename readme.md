# Bio Image Processing
This is currently just a sanity check to show that using 
python with OpenCv is working.  If it does not, then something 
is wrong with the configuration of the system.

## Set up
This program uses python 3.  It also uses OpenCv.  To make sure that 
you have OpenCv with the python bindings, just open a terminal and 
run :

```console
$ pip3 install opencv-python
```
  

## Running the scripts
You can do facial detection in an image by running:

```console
$ python3 CvFaceRecTest.py
```
But, for now, the path to image is hard coded.
If you would like to do facial detection using a webcam, 
just open a terminal and cd to the directory conatining the scripts.
Then enter:
```console
$ python3 CvFaceRecCamTest.py 
```
