# Music Artists Statistics

An app in Python showing the average length of an artist's song lyrics.

To install:

## On Windows

### Install the latest stable version of Python. Version 3.8 is the latest at time of writing.
Install from [Python.org](https://www.python.org/)

Go to a command prompt. The quickest way is to press Windows Key+R. 
At the Open prompt type **cmd** & press ENTER.
Note if this doesn't work you might have to run **cmd** as Administrator.

To check Python is installed:

**py**

Install pip - Python's package installer:

**py -m pip install -U pip**

Find the location where pip is installed. For me this was in my AppData\Local\Programs\Python\Python38-32\Scripts folder.

Install *requests* package:

**pip3 install requests**


## On Linux and Mac
Check if Python 3.x is already installed.
At command prompt.

**python3**

You should get a confirmation and >>> prompt.
**Ctrl+D** to exit

If not already installed, install from [Python.org](https://www.python.org/)

Note: On a Mac I got the problem that the 'requests' library was not installed.

*You need an administrator access.*

Install *requests* package:

**pip3 install requests**


## On all operating systems:

Download *this code* - the green button "Clone or Download Zip"
Go to location where you extracted the zip file.

To run the code on Windows:

**py program.py**

To run the code on Linux or Mac:

**python3 program.py**

## Running the program

When running the program, you will be prompted for an artist's name.
Enter a name and if found, the code will run and retrieve the songs and lyrics for that artist.
This takes a while as it checks all the artist's releases.
(Note: You need an internet connection for this to work as the code is retrieving data from other web sites).

