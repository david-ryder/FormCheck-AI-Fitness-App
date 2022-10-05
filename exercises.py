from skeleton import skeleton

def bar(langle, rangle):
    if langle > 160 and rangle > 160 :
        stage = "down"
    if langle < 30 and stage =='down' and rangle < 30 and stage =='down':
        stage="up"
        counter +=1

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

# Flags
hand_spacing = True
shoulders = True

    
# Bench press fail conditions
def benchPressCheck(skelly):
    global hand_spacing
    global shoulders

    # Head, shoulders, and glutes touching bench?

    # Hands evenly spaced?
    
    # get absolute value of the difference between shoulder and wrist X coordinates
    l_difference = abs(skelly.l_wrist[0] - skelly.l_shoulder[0])
    r_difference = abs(skelly.r_wrist[0] - skelly.r_shoulder[0])

    # the difference between these two coordinates should be close to 0 (5% margin of error)
    if (abs(l_difference - r_difference) >= 0.05):
        print('hand spacing fail')
        hand_spacing = False

    # Hands slightly more outside of shoulders?
    # wrists should be 5-15% outside of shoulders
    # left check
    if (l_difference <= skelly.l_shoulder[0] * 0.15 or l_difference >= skelly.l_shoulder[0] * 0.05):
        print('shoulder/hand fail')
        shoulders = False
    # right check
    if (r_difference <= skelly.r_shoulder[0] * 0.15 or r_difference >= skelly.r_shoulder[0] * 0.05):
        print('shoulder/hand fail')
        shoulders = False

    # Weight stays above chest?

    # Elbow angle close to 180 degrees at top?

    # Elbow angle between 45 and 75 degrees at bottom?

    # Feet flat on ground?

    