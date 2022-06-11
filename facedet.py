"import" cv2 as cv
import mediapipe as mp

detection = mp.solutions.face_detection
draw = mp.solutions.drawing_utils

cap = cv.VideoCapture(0)

with detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened:
        success, frame = cap.read()
        frame.flags.writeable = False
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = face_detection.process(frame)

        frame.flags.writeable = True
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        if results.detections:
            for detection in results.detections:
                draw.draw_detection(frame, detection)
        # Flip the image horizontally for a selfie-view display.
        cv.imshow('MediaPipe Face Detection', cv.flip(frame, 1))

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
