import sys
import threading

import cv2
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel


# Using a QLabel as the base widget instead of QWidget for this example
class MainWindow(QLabel):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("HSL | Buttons and Widgets")
        self.setWindowIcon(QtGui.QIcon("assets/HSL-logo.png"))

        # Setting up the window and formating of any text
        self.setMinimumWidth(640)
        self.setMinimumHeight(480)
        self.setAlignment(Qt.AlignCenter)
        self.running = True

        # Retrieving the first webcam connected to the computer via OpenCV
        self.cap = cv2.VideoCapture(0)
        # Checking if the webcam exists
        if self.cap is None or not self.cap.isOpened():
            self.setText("Unable to find a webcam")
        else:
            # If the webcam exists, startup a thread which continuously reads a frame and displays it to the screen
            th = threading.Thread(target=self.show_webcam)
            th.start()

    def show_webcam(self):
        # Keep fetching and displaying frames forever
        while self.running:
            # Retriving a frame from the webcam
            ret, frame = self.cap.read()
            # Checking if OpenCV could get a frame
            if not ret:
                continue

            # Converting the image (numpy array) into a QImage for displaying
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)

            # Resizing the image to fit the screen
            sz = self.size()
            p = convertToQtFormat.scaled(sz.width(), sz.height(), Qt.KeepAspectRatio)

            # Displaying the frame on the main widget (self)
            self.setPixmap(QPixmap.fromImage(p))

    def shutdown(self):
        self.running = False


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    e_code = app.exec_()
    window.shutdown()  # Calling MainWindow.shutdown to cleanup the video handling thread
    sys.exit(e_code)


if __name__ == '__main__':
    main()

