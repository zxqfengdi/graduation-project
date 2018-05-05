# coding:utf-8
"""
@author: fengdi
@date: 2018-04-19 15:20
@file: firstwindow.py
"""

import sys
from PyQt5.QtWidgets import (QDialog, QGraphicsView, QApplication, QLabel,
                             QPushButton, QFrame)


class FirstWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setui()

    def setui(self):
        self.setWindowTitle("人脸检测")
        self.setGeometry(200, 50, 970, 570)

        self.label1 = QLabel("原始图片", self)
        self.label1.setGeometry(200, 10, 81, 21)

        self.label2 = QLabel("识别结果", self)
        self.label2.setGeometry(680, 10, 81, 21)

        self.graphview1 = QGraphicsView(self)
        self.graphview1.setGeometry(40, 40, 431, 431)

        self.graphview2 = QGraphicsView(self)
        self.graphview2.setGeometry(500, 40, 431, 431)

        self.label3 = QLabel("", self)
        self.label3.setGeometry(70, 70, 371, 371)

        self.label4 = QLabel("", self)
        self.label4.setGeometry(535, 70, 371, 371)

        self.line = QFrame(self)
        self.line.setGeometry(460, 40, 51, 431)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.bt1 = QPushButton("选择图片", self)
        self.bt1.setGeometry(200, 490, 91, 31)

        self.bt2 = QPushButton("检测图片", self)
        self.bt2.setGeometry(670, 490, 91, 31)

        self.bt3 = QPushButton("关闭", self)
        self.bt3.setGeometry(850, 530, 91, 31)

        self.bt3.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    first_window = FirstWindow()
    first_window.show()
    sys.exit(app.exec_())
