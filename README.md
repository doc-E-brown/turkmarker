# MechTurkLandmarker  [![travisCI](https://travis-ci.org/benjohnston24/MechTurkLandmarker.svg?branch=master)](https://travis-ci.org/benjohnston24/MechTurkLandmarker)  [![codecov](https://codecov.io/gh/benjohnston24/MechTurkLandmarker/branch/master/graph/badge.svg)](https://codecov.io/gh/benjohnston24/MechTurkLandmarker)
## Manual Image Landmarking in Amazon Mechanical Turk

MechTurkLandmarker is a web-based image landmarking tool intended for use with Amazon Mechanical Turk.  With MechTurkLandmarker you can easily submit tasks to Amazon Mechanical Turk, allowing for many people to manually identify landmarks of interest on an image. This automatically 'package' generates all of the
required files and automates the build and deployment process through through pre-configured Python scripts.  The default setup provides all of the
files required in order to create a Mechanical Turk HIT to landmark an example face with the [MULTI-PIE landmark
configuration](http://www.flintbox.com/public/project/4742/).  An example of a deployed HIT to Amazon S3 can be found
[here](https://s3-us-west-2.amazonaws.com/turklandmarker/index.html)

# Installation

Currently the source has not been organised into a single Python package for download from pypi, this may occur in the
future with continued development, if there is sufficient demand.  For now, simply clone the entire source directory and
install all the requirements.  It is always recommended to use a virtualenv when installing all requirements.

```
git clone git@github.com:benjohnston24/MechTurkLandmarker.git
cd MechTurkLandmarker
pip install -r requirements.txt
```

## Configuration Files

* [.configrc](https://github.com/benjohnston24/MechTurkLandmarker/blob/master/.configrc) - configuration file for the
  system, modify this file to change aspects of operation and details of the Mechanical Turk HIT tasks or S3 Buckets. 

## Building

## TODO

* Improve test coverage - Python
* Add javascript unit tests
* Add multi-image HITS 
