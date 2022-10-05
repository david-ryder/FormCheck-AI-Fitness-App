import cv2, random, exercises
import mediapipe as mp
import numpy as np
from skeleton import skeleton

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

print("0: Bar\n1: Curl left\n2: Curl right\n3: Bench")
exchoice = int(input()) #front end problem :/

cap = cv2.VideoCapture(0)

# Curl counter variables
counter = 0 
stage = None

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        try:
            skelly = skeleton(mp_pose, results.pose_landmarks.landmark)
            
            # Calculate angle
            langle = skelly.calcuate_lelbow()
            rangle = skelly.calcuate_relbow()
                
            # Visualize angle
            cv2.putText(image, str(langle), tuple(np.multiply(skelly.lelbow, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(rangle), tuple(np.multiply(skelly.relbow, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            if exchoice == 0:         
                exercises.bar(langle, rangle)
            elif exchoice == 1:                
                exercises.curl(langle)
            elif exchoice == 2:
                exercises.curl(rangle)
            elif exchoice == 3:
                exercises.benchPress(langle, rangle)

            # Setup bench press fail checking
            if exchoice == 'bench_press':
                exercises.benchPressCheck(skelly)

        except:
            pass

        # Render curl counter
        # Setup status box
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        # Rep data
        cv2.putText(image, 'REPS', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        # Stage data
        cv2.putText(image, 'STAGE', (65,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, 
                    (60,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Cam', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
