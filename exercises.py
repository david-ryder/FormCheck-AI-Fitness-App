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