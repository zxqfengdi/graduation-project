# coding:utf-8
"""
@author: fengdi
@date: 2018-04-19 18:45
@file: run.py
"""

import sys
from PyQt5.QtWidgets import QApplication
from project_ui.mainwindow import MainWindow
from project_code.detection import FaceDetection
from project_code.recognition import FaceRecognition
from project_code.camera import CameraRecognize


class MyMainWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.setui()


class MyFirstWindow(FaceDetection):
    def __init__(self):
        super().__init__()
        self.setui()


class MySecondWindow(FaceRecognition):
    def __init__(self):
        super().__init__()
        self.setui()


class MyThirdWindow(CameraRecognize):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    my_main_window = MyMainWindow()
    my_first_window = MyFirstWindow()
    my_second_window = MySecondWindow()
    my_third_window = MyThirdWindow()

    my_main_window.bt1.clicked.connect(my_first_window.open_window)
    my_main_window.bt2.clicked.connect(my_second_window.open_window)
    my_main_window.bt3.clicked.connect(my_third_window.camera_recognize)

    my_first_window.bt1.clicked.connect(my_first_window.open_image)
    my_first_window.bt2.clicked.connect(my_first_window.detect_image)

    my_second_window.bt1.clicked.connect(my_second_window.open_image)
    my_second_window.bt2.clicked.connect(my_second_window.recognize_image)

    my_main_window.show()
    sys.exit(app.exec_())
