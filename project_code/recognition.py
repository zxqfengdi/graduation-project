# coding:utf-8
"""
@author: fengdi
@file: recognition.py
@time: 2018-04-21 15:55
"""

import sys, face_recognition
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from project_ui.secondwindow import SecondWindow
from PyQt5.QtWidgets import QFileDialog, QApplication

image_name = ""


class FaceRecognition(SecondWindow):
    def __init__(self):
        super().__init__()
        self.setui()

    def open_image(self):
        global image_name

        image_name = QFileDialog.getOpenFileName(
            self, "打开图片", "./", "Image Files(*.jpg *.jpeg *.png)")[0]
        image = QPixmap(image_name).scaled(self.label3.width(),
                                           self.label3.height())
        self.label3.setPixmap(image)

    def recognize_image(self):

        if not image_name:
            self.label4.setAlignment(Qt.AlignCenter)
            self.label4.setText("请选择要检测的图片！！")
        else:
            jobs_image = face_recognition.load_image_file(
                "/media/fengdi/数据/graduation-project/facedata/jobs.png")
            curry_image = face_recognition.load_image_file(
                "/media/fengdi/数据/graduation-project/facedata/curry.jpg")
            putin_image = face_recognition.load_image_file(
                "/media/fengdi/数据/graduation-project/facedata/putin.jpeg")
            xidada_image = face_recognition.load_image_file(
                "/media/fengdi/数据/graduation-project/facedata/xidada.jpg")

            # jobs_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\jobs.png")
            # curry_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\curry.jpg")
            # putin_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\putin.jpeg")
            # xidada_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\xidada.jpg")

            jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
            curry_encoding = face_recognition.face_encodings(curry_image)[0]
            putin_encoding = face_recognition.face_encodings(putin_image)[0]
            xidada_encoding = face_recognition.face_encodings(xidada_image)[0]

            unknown_image = face_recognition.load_image_file(image_name)
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            encoding_list = [jobs_encoding, curry_encoding, putin_encoding, xidada_encoding]
            results = face_recognition.compare_faces(encoding_list, unknown_encoding)
            labels = ['乔布斯', '库里', '普京', '习近平']

            for i in range(len(results)):
                if results[i]:
                    self.label4.setAlignment(Qt.AlignCenter)
                    self.label4.setText("检测到人物：" + labels[i])

    def open_window(self):
        if not self.isVisible():
            self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    second_window = FaceRecognition()

    second_window.bt1.clicked.connect(second_window.open_image)
    second_window.bt2.clicked.connect(second_window.recognize_image)

    second_window.show()
    sys.exit(app.exec_())