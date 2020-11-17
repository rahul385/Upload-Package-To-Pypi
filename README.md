# Upload-Package-To-Pypi

### Table of Contents
1. [Blog Post](https://medium.com/@rahulgupta1/upload-your-python-package-to-pypi-c45ad6a52a13)
2. [Installation](#installation)
3. [Project Motivation](#motivation)
4. [File Descriptions](#files)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
Install the package by running the following command

`pip install nearest-square`

## Project Motivation<a name="motivation"></a>

For this project, I was interested in creating and publishing a simple package to pypi.
Pypi is a is a repository of software for the Python programming language. It is used by Python developers to to publicize and share their software.

Once uploaded to pypi, the package can be used by all Python users after installing it. Below is the sample usage:
```
>>> from nearest_square import nearest_square as nsqr
>>> nsqr(101)
100
```

## File Descriptions <a name="files"></a>

* Upload-Package-To-Pypi : Container folder, includes the following files:
    * `license.txt` : License
    * `Readme.md` : Description of the package and its usage
    * `setup.py` : Contains name of the package and author's information
* nearest_square: Includes all package files
    * `__init__.py` : Initialization file
    * `nearest_square.py` : Python file containing actual program/code
    * `setup.cfg` : Setup file

## Licensing, Authors, Acknowledgements<a name="licensing"></a>
Author: Rahul Gupta
