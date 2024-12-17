from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import dlib
import os
from imutils import face_utils

# Inisialisasi deteksi wajah
predictor_path = os.path.join(os.path.dirname(__file__), 'models', 'shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

# Fungsi untuk merender halaman webcam
def webcam_view(request):
    return render(request, 'webcam.html')

# Fungsi untuk men-stream webcam feed dengan deteksi wajah
def webcam_feed(request):
    cap = cv2.VideoCapture(0)  # Akses webcam (0 berarti webcam default)

    def generate_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Konversi ke grayscale
            faces = detector(gray)  # Deteksi wajah

            # Loop untuk menggambar kotak di sekitar wajah yang terdeteksi
            for face in faces:
                (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
                shape = predictor(gray, face)
                shape = face_utils.shape_to_np(shape)

                # Gambarkan landmark wajah
                for (x, y) in shape:
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

                # Gambarkan kotak di sekitar wajah
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Encode frame ke JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Kirim frame ke browser
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
