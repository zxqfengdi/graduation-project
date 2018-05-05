# coding:utf-8
"""
@author: fengdi
@date: 2018-04-20 18:22
@file: detection.py
"""

import cv2, sys, face_recognition
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from project_ui.firstwindow import FirstWindow
from PyQt5.QtWidgets import QFileDialog, QApplication

image_name = ""


class FaceDetection(FirstWindow):
    def __init__(self):
        super().__init__()
        self.setui()

    def open_image(self):
        global image_name

        image_name = QFileDialog.getOpenFileName(self, "打开图片", "./", "Image Files(*.jpg *.jpeg *.png)")[0]
        image = QPixmap(image_name).scaled(self.label3.width(), self.label3.height())
        self.label3.setPixmap(image)

    def detect_image(self):
        if not image_name:
            self.label4.setAlignment(Qt.AlignCenter)
            self.label4.setText("请选择要检测的图片！！")
        else:
            image = face_recognition.load_image_file(image_name)
            face_locations = face_recognition.face_locations(image)
            image01 = cv2.imread(image_name, cv2.IMREAD_COLOR)

            for face_location in face_locations:
                top, right, bottom, left = face_location

                start = (left, top)
                end = (right, bottom)
                color = (0, 255, 0)
                thickness = 2

                cv2.rectangle(image01, start, end, color, thickness)

            cv2.imwrite(r"/media/fengdi/数据/graduation-project/model/" + image_name.split("/")[-1], image01)
            image = QPixmap(r"/media/fengdi/数据/graduation-project/model/" + image_name.split("/")[-1]).scaled(self.label4.width(), self.label4.height())
            self.label4.setPixmap(image)

            # cv2.imwrite("E:\graduation-project\model\\" + image_name.split("/")[-1], image01)
            # image = QPixmap("E:\graduation-project\model\\" + image_name.split("/")[-1]).scaled(self.label4.width(), self.label4.height())
            # self.label4.setPixmap(image)

    def open_window(self):
        if not self.isVisible():
            self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    first_window = FaceDetection()

    first_window.bt1.clicked.connect(first_window.open_image)
    first_window.bt2.clicked.connect(first_window.detect_image)

    first_window.show()
    sys.exit(app.exec_())
