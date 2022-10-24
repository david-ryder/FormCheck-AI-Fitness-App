from skeleton import skeleton

# Margin of error constant
MOE = 0.1


def bar(langle, rangle):
    if langle > 160 and rangle > 160 :
        stage = "down"
    if langle < 30 and stage =='down' and rangle < 30 and stage =='down':
        stage="up"
        counter += 1

def curl(angle):
    if angle > 160:
        stage = "down"
    if angle < 30 and stage =='down':
        stage="up"
        counter +=1

def benchPress(langle, rangle):
    if langle > 165 and rangle > 165 :
        stage = "up"
    if langle < 65 and stage =='up' and rangle < 65 and stage =='up':
        stage="down"
        counter +=1

# Calculates the percent difference between two points
def getPercentDifference(a, b):
    abs_difference = abs(a - b) # absolute value of difference
    average = (a + b) / 2 # average of 2 offsets
    percent_difference = abs_difference / average
    return percent_difference

# Fail flags - Bench Press
hand_spacing = True
shoulders = True
arms_straight = True
elbows_apart = True

# Continuous variables
elbow_left_up = 0
elbow_left_down = 1000000
elbow_right_up = 0
elbow_right_down = 1000000

# Bench press fail conditions
def benchPressCheck(skelly, stage):
    global hand_spacing
    global shoulders
    global arms_straight
    global elbows_apart

    global elbow_left_up
    global elbow_left_down
    global elbow_right_up
    global elbow_right_down

    # Hands evenly spaced?
    center = (skelly.l_shoulder[0] + skelly.r_shoulder[0]) / 2 # get center of shoulders

    l_offset = abs(center - skelly.l_wrist[0])
    r_offset = abs(center - skelly.r_wrist[0])

    percent_difference = getPercentDifference(l_offset, r_offset)

    if (percent_difference <= MOE): # fail condition
        hand_spacing = False
        print('hand spacing uneven')

    # Hands slightly more outside of shoulders?
    l_wrist = skelly.l_wrist[0]
    l_shoulder = skelly.l_shoulder[0]

    if (not (l_wrist <= l_shoulder * 0.95 and l_wrist >= l_shoulder * 0.85)): # left check
        shoulders = False
        print('hands are not between 5-15 percent outside of shoulders, left')

    r_wrist = skelly.r_wrist[0]
    r_shoulder = skelly.r_shoulder[0]

    if (not (r_wrist >= r_shoulder * 1.05 and r_wrist <= r_shoulder * 1.15)): # right check
        shoulders = False
        print('hands are not between 5-15 percent outside of shoulders, right')

    # Elbow angle close to 180 degrees at top? Shoulder angle between 45 and 75 degrees at bottom?
    # update the up angle when stage is up, but do failcheck for down
    if (stage == 'up'):
        # update up
        elbow_left_up = max(elbow_left_up, skelly.calcuate_lelbow())
        elbow_right_up = max(elbow_right_up, skelly.calcuate_relbow())

        # failcheck for down - reset down angle
        if (not((elbow_left_down >= 45) and (elbow_left_down <= 75))):
            arms_straight = False
            print('elbows are not between 45 and 75 degrees when weight is down, left')
        if (not((elbow_right_down >= 45) and (elbow_right_down <= 75))):
            arms_straight = False
            print('elbows are not between 45 and 75 degrees when weight is down, right')
        elbow_left_down = 0
        elbow_right_down = 0


    # update the down angle when stage is down, but do failcheck for up
    if (stage == 'down'):
        # update down
        elbow_left_down = min(elbow_left_down, skelly.calculate_lshoulder())
        elbow_right_down = min(elbow_right_down, skelly.calculate_rshoulder())

        # failcheck for up - reset up angle
        if (not((elbow_left_up >= 170) and (elbow_left_up <= 180))):
            arms_straight = False
            print('not fully extending on up, left')
        if (not((elbow_right_down >= 170) and (elbow_right_down <= 180))):
            arms_straight = False
            print('not fully extending on up, left')
        elbow_left_up = 0
        elbow_right_up = 0

# Fail flags - Deadlifts
feet = True
straightLegs = True
handPlacement = True
bendingBack = True

# Continuous variables
l_leg = 0
r_leg = 0

def deadliftCheck(skelly, stage):
    global feet
    global straightLegs
    global handPlacement
    global bendingBack

    global l_leg
    global r_leg

    # feet shoulder width apart? allow margin of error outside of body
    l_ankle = skelly.l_ankle[0]
    r_ankle = skelly.r_ankle[0]

    l_shoulder = skelly.l_shoulder[0]
    r_shoulder = skelly.r_shoulder[0]

    if (not (l_ankle <= l_shoulder and l_ankle >= l_shoulder * (1 - MOE))): # left check
        feet = False
        print('feet not about shoulder width apart')

    if (not (r_ankle >= r_shoulder and r_ankle <= r_shoulder * (1 + MOE))): # right check
        feet = False
        print('feet not about shoulder width apart')

    if (stage == 'up'):
        # update up position
        l_leg = max(l_leg, skelly.calculate_lknee())
        r_leg = max(r_leg, skelly.calculate_rknee())

        # failcheck for down
        l_knee = skelly.l_knee[0]
        r_knee = skelly.r_knee[0]
        l_wrist = skelly.l_wrist[0]
        r_wrist = skelly.r_wrist[0]

        # hands outside of knees? between 5 and 15% outside
        if (not (l_wrist <= l_knee * 0.95 and l_wrist >= l_knee * 0.85)): # left check
            handPlacement = False
            print('hands not between 5 and 15 percent outside of knee, left')
        if (not (r_wrist <= r_knee * 0.95 and r_wrist >= r_knee * 0.85)): # right check
            handPlacement = False
            print('hands not between 5 and 15 percent outside of knee, right')

    if (stage == 'down'):
        # failcheck for up
        if (not((l_leg >= 170) and (l_leg <= 180))):
            straightLegs = False
            print('not fully extending on up, left')
        if (not((r_leg >= 170) and (r_leg <= 180))):
            straightLegs = False
            print('not fully extending on up, left')
        l_leg = 0
        r_leg = 0

        # failcheck for knee - shoulder depth
        if (not(skelly.l_knee[2] <= skelly.l_shoulder[2] * (1 + MOE) and skelly.l_knee[2] >= skelly.l_shoulder[2] * (1 - MOE))):
            bendingBack = False
            print('back bending, left')
        if (not(skelly.r_knee[2] <= skelly.r_shoulder[2] * (1 + MOE) and skelly.r_knee[2] >= skelly.r_shoulder[2] * (1 - MOE))):
            bendingBack = False
            print('back bending, right')

ddown=0
pole=0
def pullupcheck(skelly, stage):
    global ddown
    global pole
    langle = skelly.calcuate_lelbow()
    rangle = skelly.calcuate_relbow()
    if stage=='up':
        if (skelly.l_elbow[1] > skelly.l_shoulder[1]) and (skelly.r_elbow[1] > skelly.r_shoulder[1]) and langle>50 and rangle>50:
            print("hands too wide", langle, rangle)
        if (skelly.l_wrist[1]>skelly.mouth[1]):
            pole=0
        else:
            pole+=1
    if stage=='down':
        if langle<150 or rangle<150:
            ddown+=1
    
    
    
    