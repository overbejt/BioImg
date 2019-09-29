# Bio Image Processing
This is currently just a sanity check to show that using 
python with OpenCv is working.  If it does not, then something 
is wrong with the configuration of the system.

## Set up
It is assumed that OpenCv is already installed on the machine.  This program uses python 3.  It also uses OpenCv.  To make sure that 
you have OpenCv with the python bindings, just open a terminal and 
run :

```console
$ pip3 install opencv-python
```

It does use numpy as a dependency.  To make sure that you have it 
installed, enter:

```console
$ pip3 install numpy
```
  

## Running the scripts
You can do facial detection in an image by running:

```console
$ python3 CvFaceRecTest.py <name of file>
```
For example you could run, 

```console
$ python3 CvFaceRecTest.py images/simple.jpg
```
All of the images are stored in the images folder.
If you would like to do facial detection using a webcam, 
just open a terminal and cd to the directory containing the scripts.
Then enter:
```console
$ python3 CvFaceRecCamTest.py 
```
