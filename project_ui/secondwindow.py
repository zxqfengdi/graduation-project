# coding:utf-8
"""
@author: fengdi
@date: 2018-04-19 19:44
@file: secondwindow.py
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QPushButton, QGraphicsView


class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setui()

    def setui(self):
        self.setWindowTitle("人脸识别")
        self.resize(993, 557)

        self.label1 = QLabel("原始图片", self)
        self.label1.setGeometry(180, 20, 91, 31)

        self.label2 = QLabel("识别结果", self)
        self.label2.setGeometry(690, 20, 91, 31)

        self.graphview1 = QGraphicsView(self)
        self.graphview1.setGeometry(20, 70, 421, 441)

        self.graphview2 = QGraphicsView(self)
        self.graphview2.setGeometry(550, 70, 421, 441)

        self.label3 = QLabel("", self)
        self.label3.setGeometry(45, 110, 371, 371)

        self.label4 = QLabel("", self)
        self.label4.setGeometry(576, 110, 371, 371)

        self.bt1 = QPushButton("选择图片", self)
        self.bt1.setGeometry(450, 110, 91, 31)

        self.bt2 = QPushButton("识别图片", self)
        self.bt2.setGeometry(450, 280, 91, 31)

        self.bt3 = QPushButton("关闭", self)
        self.bt3.setGeometry(450, 440, 91, 31)

        self.bt3.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    second_window = SecondWindow()
    second_window.show()
    sys.exit(app.exec_())