# Buttons and Widgets

### Overview

This sample application introduces two new concepts; layouts and widgets.  Widgets are the basic building blocks in PyQt.
It can contain UI elements such as textboxes, buttons, sliders, images, etc.  They are able to support basic user
interaction by emitting a signal when interacted with.  You can then create functions which gets triggered by those
signals in an event based system.

But widgets on their own are fairly useless.  To make anything complex in PyQt, you will need to be able to combine
widgets together, ie. press a button and display some text in a textbox, etc.  In PyQt, the visual aspect of this can
be done using layouts.

A layout can be used to arrange multiple widgets together in a specific orientation.  For example, you can use a
```QHBoxLayout``` to arrange multiple widgets side by side horizontally.  And similarly you can use a ```QVBoxLayout```
to arrange multiple widgets vertically.  Furthermore, after you have defined a layout, you can create a widget from
that layout which can then be used within another layout.
 
In the example provided, a ```QVBoxLayout``` is used to combine four ```QPushButton``` widgets into a vertical widget.
This widget is then combined with a ```QTextEdit``` widget in a ```QHBoxLayout``` to create the overall window.  The
buttons are then connected to handler functions which modify the textbox differently depending on the button pressed.

### Challenges

 - Look through the various [widgets](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/index.html) that PyQt5 provides,
and try to use one in an application
 - Try to build an application using [```QMainWindow```](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMainWindow.html)
as the base class of your ```MainWindow```, and try using the features it provides
 - Create an application which displays an image on a widget
