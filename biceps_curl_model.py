import cv2
import mediapipe as mp
import numpy as np
def calculation(a,b,c):
  a=np.array(a)
  b=np.array(b)
  c=np.array(c)

  radians=np.arctan2(c[1]-b[1],c[0]-b[0])-np.arctan2(a[1]-b[1],a[0]-b[0])
  angle=np.abs(radians*180/np.pi)
  if angle>180:
    angle=360-angle
  
  return angle

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose
cap=cv2.VideoCapture(0)
count_left,count_right=0,0
stage_left,stage_right=None,None

with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    ret,frame=cap.read()

    image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    image.flags.writeable=False

    result=pose.process(image)

    image.flags.writeable=True
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    try:
      landmarks=result.pose_landmarks.landmark

      shoulder_right=[landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
      elbow_right=[landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
      wrist_right=[landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

      shoulder_left=[landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
      elbow_left=[landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
      wrist_left=[landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

      angle_left=calculation(shoulder_left,elbow_left,wrist_left)
      angle_right=calculation(shoulder_right,elbow_right,wrist_right)

      cv2.putText(image,f"{angle_left:.2f}",tuple(np.multiply(elbow_left,[640,480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
      cv2.putText(image,f"{angle_right:.2f}",tuple(np.multiply(elbow_right,[640,480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)

      if angle_left>160:
        stage_left='down'
      if angle_left<10 and stage_left=='down':
        stage_left='up'
        count_left+=1

      if angle_right>160:
        stage_right='down'
      if angle_right<10 and stage_right=='down':
        stage_right='up'
        count_right+=1

    except:
      pass
    
    # Right side counter
    cv2.rectangle(image, (0, 0), (200, 100), (245, 93, 100), -1)
    cv2.putText(image, 'RIGHT REPS', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(count_right), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, 'STAGE', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(stage_right), (90, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    # Left side counter
    cv2.rectangle(image, (440, 0), (640, 100), (245, 93, 100), -1)
    cv2.putText(image, 'LEFT REPS', (450, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(count_left), (450, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, 'STAGE', (450, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(stage_left), (530, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    mp_drawing.draw_landmarks(image,result.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(245,117,66),thickness=2,circle_radius=2),
                              mp_drawing.DrawingSpec(color=(245,66,230),thickness=2,circle_radius=2))

    cv2.imshow('mediapipe feed',image)
    if cv2.waitKey(10) & 0xFF==ord('q'):
      break
    if cv2.waitKey(1) & 0xFF==ord('r'):
      count_left,count_right=0,0
cap.release()
cv2.destroyAllWindows()