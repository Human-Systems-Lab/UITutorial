# import python standard library modules/packages first
import sys

# import external libraries second
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

# import project specific modules/packages last (we don't have any for this project)


# Class that represents your window and the data that it contains
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("HSL | Getting Started")
        self.setWindowIcon(QtGui.QIcon("assets/HSL-logo.png"))


def main():
    # Standard logic for creating and displaying your MainWindow
    app = QApplication(sys.argv)  # Create a new instance of a PyQt application
    window = MainWindow()         # Create an instance of the window you defined above
    window.show()                 # Display the window to the screen
    e_code = app.exec_()          # Run the application event loop
    sys.exit(e_code)              # Terminate the program


# This ensures that the main function is run only if this module is run as the entry point
if __name__ == '__main__':
    main()
