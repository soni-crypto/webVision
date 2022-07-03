
import mediapipe as mp
import cv2
from flask import Blueprint, Response

def cuerpoCV2():
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#"routes/videos/vid5.mp4")
    mp_drawing=mp.solutions.drawing_utils
    mp_pose=mp.solutions.pose
    with mp_pose.Pose(static_image_mode=False) as pose:
        while True:
            state, frame=cap.read()
            if state:
                # frame=cv2.flip(frame, 1)
                frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resultado=pose.process(frameRGB)
                if resultado.pose_landmarks is not None:
                    mp_drawing.draw_landmarks(frame, resultado.pose_landmarks, mp_pose.POSE_CONNECTIONS )
                cv2.waitKey(2)
                (tag, encodedImage)=cv2.imencode(".jpg", frame)
                if not tag:
                    continue
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                        bytearray(encodedImage) + b'\r\n')

formatoVideo4=Blueprint("formatoVideo4", __name__)
@formatoVideo4.route("/pose")
def video_feed4():
    return Response(cuerpoCV2(), mimetype="multipart/x-mixed-replace; boundary=frame")