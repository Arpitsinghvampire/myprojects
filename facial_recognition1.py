import cv2 as cv
import mediapipe as mp
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_face_mesh=mp.solutions.face_mesh
drawing_spec=mp_drawing.DrawingSpec(thickness=1,circle_radius=1)
cap=cv.VideoCapture(0)
with mp_face_mesh.FaceMesh(max_num_faces=1,refine_landmarks=True,min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success,image=cap.read()
        if not success:
            print("READING EMPTY FRAMES")
            continue
        image.flags.writeable=False
        image=cv.cvtColor(image,cv.COLOR_BGR2RGB)
        results=face_mesh.process(image)
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_iris_connections_style())
    # Flip the image horizontally for a selfie-view display.
        cv.imshow('MediaPipe Face Mesh', cv.flip(image,1))
        if cv.waitKey(5) & 0xFF == 27:
            break
cap.release()

'''image.flags.writeable=True
        image=cv.cvtColor(image,cv.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(image=image,landmarks_list=face_landmarks,landmarks_drawing_spec=None,connections=mp_face_mesh.FACEMESH_TESSELATION,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(image=image,landmarks_list=face_landmarks,landmarks_drawing_spec=None,connections=mp_face_mesh.FACEMESH_CONTOURS,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(image=image,landmarks_list=face_landmarks,landmarks_drawing_spec=None,connections=mp_face_mesh.FACEMESH_IRISES,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_style())
        cv.imshow("FACIAL MESH RECOGNITION",cv.flip(image,1))
        if cv.waitKey(5)  and 0xFF==27:
            break
cap.release()'''
        