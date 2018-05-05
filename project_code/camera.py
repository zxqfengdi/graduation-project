# coding:utf-8
"""
@author: fengdi
@file: camera.py
@time: 2018-04-21 22:12
"""

import cv2
import face_recognition


class CameraRecognize(object):
    def __init__(self):
        super().__init__()

    def camera_recognize(self):
        video_capture = cv2.VideoCapture(1)

        jobs_image = face_recognition.load_image_file("/media/fengdi/数据/graduation-project/facedata/jobs.png")
        curry_image = face_recognition.load_image_file("/media/fengdi/数据/graduation-project/facedata/curry.jpg")
        putin_image = face_recognition.load_image_file("/media/fengdi/数据/graduation-project/facedata/putin.jpeg")
        # xidada_image = face_recognition.load_image_file("/media/fengdi/数据/graduation-project/facedata/xidada.jpg")

        # jobs_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\jobs.png")
        # curry_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\curry.jpg")
        # putin_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\putin.jpeg")
        # xidada_image = face_recognition.load_image_file(r"E:\graduation-project\facedata\xidada.jpg")

        jobs_face_encoding = face_recognition.face_encodings(jobs_image)[0]
        curry_face_encoding = face_recognition.face_encodings(curry_image)[0]
        putin_encoding = face_recognition.face_encodings(putin_image)[0]
        # xidada_encoding = face_recognition.face_encodings(xidada_image)[0]

        known_face_encodings = [jobs_face_encoding, curry_face_encoding, putin_encoding]
        known_face_names = ["jobs", "curry", "putin"]

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            if process_this_frame:
                face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)

                face_names = []

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(
                        known_face_encodings, face_encoding)
                    name = "unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame

            for (top, right, bottom, left), name in zip(
                    face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                start = (left, top)
                end = (right, bottom)
                color = (0, 255, 0)
                thickness = 1

                cv2.rectangle(frame, start, end, color, thickness)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom),
                              (128, 128, 128), cv2.FILLED)
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, name, (left + 30, bottom - 10), font, 1.0,
                            (0, 0, 0), 1)

            cv2.imshow('camera', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    camera = CameraRecognize()
    camera.camera_recognize()
