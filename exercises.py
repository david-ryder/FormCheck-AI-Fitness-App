from tkinter.filedialog import LoadFileDialog
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

# Margin of error variable
MOE = 0.1

# Flags
hand_spacing = True
shoulders = True

<<<<<<< Updated upstream
=======
# Calculates the percent difference between two points
def getPercentDifference(a, b):
    abs_difference = abs(a - b) # absolute value of difference
    average = (a + b) / 2 # average of 2 offsets
    percent_difference = abs_difference / average
    return percent_difference

>>>>>>> Stashed changes
# Bench press fail conditions
def benchPressCheck(skelly):
    global hand_spacing
    global shoulders

    # Head, shoulders, and glutes touching bench?

    # Hands evenly spaced?
    center = (skelly.l_shoulder[0] + skelly.r_shoulder[0]) / 2 # get center of shoulders

    l_offset = abs(center - skelly.l_wrist[0])
    r_offset = abs(center - skelly.r_wrist[0])

    percent_difference = getPercentDifference(l_offset, r_offset)

    if (percent_difference <= MOE): # fail condition
        hand_spacing = False
        print('hand spacing uneven')

    # Hands slightly more outside of shoulders?
    l_distance = skelly.l_shoulder[0] - skelly.l_wrist[0]
    r_distance = skelly.r_wrist[0] - skelly.r_shoulder[0]

    # hands should be about 5-15% outside of shoulders
    

    # Weight stays above chest?

    # Elbow angle close to 180 degrees at top?

    # Elbow angle between 45 and 75 degrees at bottom?

    # Feet flat on ground?

    