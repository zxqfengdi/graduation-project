# coding:utf-8
"""
@author: fengdi
@date: 2018-04-19 13:53
@file: mainwindow.py
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setui()

    def setui(self):
        self.setWindowTitle("人脸识别系统")
        self.resize(593, 221)

        self.bt1 = QPushButton("人脸检测", self)
        self.bt1.setGeometry(20, 80, 111, 31)

        self.bt2 = QPushButton("人脸识别", self)
        self.bt2.setGeometry(230, 80, 111, 31)
        self.bt3 = QPushButton("摄像头识别", self)
        self.bt3.setGeometry(460, 80, 111, 31)

        self.bt4 = QPushButton("关闭", self)
        self.bt4.setGeometry(470, 180, 91, 31)

        self.bt4.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
