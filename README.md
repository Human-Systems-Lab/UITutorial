# UI Programming in Python

### Introduction

There are many tools available in Python for creating graphical user interfaces (GUIs) in python.
Some of the popular toolkits are:
 - [DearPyGui](https://github.com/hoffstadt/DearPyGui)
 - [Kivy](https://kivy.org/#home)
 - [TKInter](https://docs.python.org/3/library/tkinter.html)
 - [VTK](https://vtk.org/)

Most of the above toolkits are python extensions which wrap C/C++ toolkits, and are all well featured.  But this
repository will focus specifically on [PyQt5](https://doc.qt.io/qtforpython/), a Python extension for [Qt5](https://www.qt.io/).

# Setup

To get started, you will need git to download this repository onto your computer.  You can download git [here](https://git-scm.com/downloads).
Once you have git downloaded, open a terminal/command shell and navigate to your preferred directory, then run the
following command.

```shell script
$ git clone https://github.com/Human-Systems-Lab/UITutorial.git
```

After you have this repository downloaded, you will need to setup a python environment and install both pyqt5 and opencv.
If you do not have python, you can download it from [here (PSF)](https://www.python.org/downloads/) or
[here (anaconda)](https://www.anaconda.com/products/individual). 

```shell script
$ pip install PyQt5 opencv-python
```
