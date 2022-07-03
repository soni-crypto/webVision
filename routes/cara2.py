
from flask import Blueprint, Response
import cv2
import mediapipe as mp
def cara2Cv2():
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#"routes/videos/vid3.mp4"
    mp_drawing=mp.solutions.drawing_utils
    mp_face=mp.solutions.face_detection
    with mp_face.FaceDetection(min_detection_confidence=0.5
                               ) as faceDetection:
        while True:
            state, frame=cap.read()
            if state:
                # frame=cv2.flip(frame, 1)
                frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resultado=faceDetection.process(frameRGB)
                if resultado.detections is not None:
                    for puntos in resultado.detections:
                        mp_drawing.draw_detection(frame, puntos, mp_drawing.DrawingSpec(color=(200,100,10),thickness=2, circle_radius=1), mp_drawing.DrawingSpec(color=(0, 255, 255)))
                
                cv2.waitKey(25)
                (flag, encodedImage) = cv2.imencode(".jpg",frame)
                if not flag:
                    continue
                yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                        bytearray(encodedImage) + b'\r\n')
# cap.release()
    
formatoVideoCara2=Blueprint("formatoVideoCara2", __name__)
@formatoVideoCara2.route("/video_feed2")
def video_feed2():
    return Response(cara2Cv2(), mimetype="multipart/x-mixed-replace; boundary=frame")