import cv2
import numpy as np
import face_recognition
import os
from  datetime import datetime

"""(SRH) -----------ARRANGING IMAGES AUTOMARICALLY--------- (SRH)"""
path = 'ImagesAttendence'
images = []
classNames = []
myList = os.listdir(path)
#print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
#print(classNames)


"""(SRH) -----------FINDING ENCODING--------- (SRH)"""
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

"""(SRH) -----------MARKING ATTENDENCE--------- (SRH)"""
def markAttendence(name):
    with open('Attendence.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dateTimeString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dateTimeString}')

#markAttendence('Hridoy')

encodeListKnown = findEncodings(images)
print('Encoding is  Completed')

"""(SRH) -----------INITIALIZING WEB-CAM--------- (SRH)"""
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmaller = cv2.resize(img,(0,0),None,0.25,0.25)
    imgSmaller = cv2.cvtColor(imgSmaller, cv2.COLOR_BGR2RGB)

#FINDING ENCODING OF OUR WEBCAM:
    facesCurFrame = face_recognition.face_locations(imgSmaller)
    encodesCurFrame = face_recognition.face_encodings(imgSmaller,facesCurFrame)

#FINDING MATCHES:
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1,x2, y2,x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,355,255),2)
            markAttendence(name)

    cv2.imshow('webcam',img)
    cv2.waitKey(1)
