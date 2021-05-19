import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("HSL | Buttons and Widgets")
        self.setWindowIcon(QtGui.QIcon("assets/HSL-logo.png"))

        # Creating the buttons on the left side of the window
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        clear = QPushButton("Clear")

        # Setting up the connections for each of the buttons (what happens when you press them)
        button1.clicked.connect(self.on_button1)
        button2.clicked.connect(self.on_button2)
        button3.clicked.connect(self.on_button3)
        clear.clicked.connect(self.on_clear)

        # Creating the textbox on the right side of the window
        self.display = QTextEdit()
        self.display.setReadOnly(True)  # Ensuring the user cannot write to it -> its only a text display
        # Setting up a string buffer for the text edit widget
        self.text = ""

        # Arranging the buttons in a vertical box layout - QVBoxLayout
        left_layout = QVBoxLayout()
        left_layout.addWidget(button1)
        left_layout.addWidget(button2)
        left_layout.addWidget(button3)
        left_layout.addWidget(clear)
        # Creating a displayable widget which contains the layout defined above
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        # Arranging the main layout,
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.display)
        self.setLayout(main_layout)

    def on_button1(self):
        # When button1 gets clicked, this function will run
        self.text += "You Pressed Button 1\n"  # Adding a line to the internal buffer
        self.display.setPlainText(self.text)   # Displaying the buffer to the screen

    def on_button2(self):
        # When button2 gets clicked, this function will run
        self.text += "You Pressed Button 2\n"  # Adding a line to the internal buffer
        self.display.setPlainText(self.text)   # Displaying the buffer to the screen

    def on_button3(self):
        # When button3 gets clicked, this function will run
        self.text += "You Pressed Button 3\n"  # Adding a line to the internal buffer
        self.display.setPlainText(self.text)   # Displaying the buffer to the screen

    def on_clear(self):
        # When the clear button gets clicked, this function will run
        self.text = ""  # Clearing the internal buffer
        self.display.setPlainText(self.text)  # Updating the screen


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    e_code = app.exec_()
    sys.exit(e_code)


if __name__ == '__main__':
    main()
