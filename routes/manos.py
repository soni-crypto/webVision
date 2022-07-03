
from flask import Blueprint, Response
import mediapipe as mp
import cv2

def manosCV2():
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#"routes/videos/vid5.mp4")
    mp_drawing=mp.solutions.drawing_utils
    mp_hands=mp.solutions.hands
    with mp_hands.Hands(static_image_mode=False, max_num_hands=4, min_detection_confidence=0.5) as hands:
        while True:
            state, frame=cap.read()
            if state:
                # frame=cv2.flip(frame, 1)
                frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resultado=hands.process(frameRGB)
                if resultado.multi_hand_landmarks is not None:
                    for puntos in resultado.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(frame, puntos, mp_hands.HAND_CONNECTIONS, 
                    mp_drawing.DrawingSpec(color=(255,0,200), thickness=2, circle_radius=3),
                    mp_drawing.DrawingSpec(color=(0,255,200), thickness=3, circle_radius=3))
                cv2.waitKey(2)
                (flag, encodedImage)=cv2.imencode(".jpg", frame)
                if not flag:
                    continue
                yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                        bytearray(encodedImage) + b'\r\n')
# cap.release()

formatoVideo3=Blueprint("formatoVideo3", __name__)
@formatoVideo3.route("/video_feed3")
def video_feed3():
    return Response(manosCV2(), mimetype="multipart/x-mixed-replace; boundary=frame")