
import mediapipe as mp
import cv2
from flask import Blueprint
from flask import Response

def detectorDeRostro():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)#"routes/videos/vid3.mp4"    
    mp_drawing=mp.solutions.drawing_utils
    mp_face=mp.solutions.face_mesh
    with mp_face.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        min_detection_confidence=0.5
        ) as faceMesh:
        
        while True:
            ret, frame = cap.read()
            if ret:
                # frame=cv2.flip(frame, 1)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result=faceMesh.process(frame_rgb)
                if result.multi_face_landmarks is not None:
                        for puntos in result.multi_face_landmarks:
                            mp_drawing.draw_landmarks(frame, puntos, mp_face.FACEMESH_TESSELATION, mp_drawing.DrawingSpec(color=(204,51,41), thickness=1, circle_radius=1), mp_drawing.DrawingSpec(color=( 255,121, 121), thickness=1))
                cv2.waitKey(20)
                    
                (flag, encodedImage) = cv2.imencode(".jpg", frame)
                if not flag:
                        continue
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                        bytearray(encodedImage) + b'\r\n')
# cap.release()

formatoVideo=Blueprint("formatoVideo", __name__)
@formatoVideo.route("/video_feed" )
def video_feed():
    
    return Response(detectorDeRostro(),
          mimetype = "multipart/x-mixed-replace; boundary=frame")
