import numpy as np

class skeleton:

    def __init__(self, mp_pose, landmarks):
        # Get coordinates
        self.l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z]
        self.r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z]
        self.l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW].y, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z]
        self.r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].y, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z]
        self.l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST].y, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z]
        self.r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z]
        self.l_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP].y, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z]
        self.r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z]
        self.l_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE].y, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z]
        self.r_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE].y, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z]
        self.l_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE].y, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z]
        self.r_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE].y, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z]
        self.mouth = [landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x, landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT].y, landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].z]

    def calcuate_lelbow(self):
        return calculate_angle(self.l_shoulder, self.l_elbow, self.l_wrist)

    def calcuate_relbow(self):
        return calculate_angle(self.r_shoulder, self.r_elbow, self.r_wrist)

    def calcuate_lshoulder(self):
        pass

    def calcuate_rshoulder(self):
        pass

    def calculate_lknee(self):
        return calculate_angle(self.l_hip, self.l_knee, self.l_ankle)

    def calculate_rknee(self):
        return calculate_angle(self.r_hip, self.r_knee, self.r_ankle)

def calculate_angle(a,b,c):
    a = np.array(a[:2]) # First
    b = np.array(b[:2]) # Mid
    c = np.array(c[:2]) # End
        
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
        
    if angle > 180.0:
        angle = 360 - angle
    return angle 
