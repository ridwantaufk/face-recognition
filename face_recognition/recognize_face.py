# import os
# import cv2
# import dlib
# from imutils import face_utils

# # Load detektor wajah dan prediktor bentuk wajah dari dlib
# predictor_path = os.path.join(os.path.dirname(__file__), 'models', 'shape_predictor_68_face_landmarks.dat')
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(predictor_path)
# # Ekspresi wajah dapat dideteksi dengan analisis keypoints atau menggunakan model yang lebih kompleks.

# def detect_faces_and_emotions():
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = detector(gray)

#         for face in faces:
#             (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
#             shape = predictor(gray, face)
#             shape = face_utils.shape_to_np(shape)

#             # Gambarkan wajah
#             for (x, y) in shape:
#                 cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

#         cv2.imshow("Face Detection", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Panggil fungsi untuk memulai deteksi wajah
# detect_faces_and_emotions()
