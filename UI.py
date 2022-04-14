import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QFileDialog, QMainWindow
from PyQt5 import uic, QtSvg
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter
#from window import Ui_window
from window2 import Ui_window


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("mainwindow.ui", self)

        # Load second window
        self.window = QMainWindow()
        self.ui = Ui_window()

        # Define Our Widgets
        self.button = self.findChild(QPushButton, "new_buttom")

        # Open Dialog box and get file path
        self.button.clicked.connect(self.clicker)

        # Show The App
        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "SVG (*.svg);;PNG (*.png);;JPEG (*.jpeg) ")[0]
        self.openWindow(fname)

    def openWindow(self, filename):
        self.ui.setupUi(self.window, filename)
        self.window.show()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
