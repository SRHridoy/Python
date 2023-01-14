import cv2
import numpy as np
import face_recognition
"""(SRH) ----------LOADING IMAGES---------- (SRH)"""
imgHridoy = face_recognition.load_image_file('ImagesBasic/hridoy.jpg')
imgHridoy = cv2.cvtColor(imgHridoy,cv2.COLOR_BGR2RGB)

"""(SRH) ----------CONVERTING BGR2RGB---------- (SRH)"""
imgHridoyTest = face_recognition.load_image_file('ImagesBasic/hridoyTest.png')
imgHridoyTest = cv2.cvtColor(imgHridoyTest,cv2.COLOR_BGR2RGB)

"""(SRH) ----------FACE-DETECTION Hridoy---------- (SRH)"""
faceLocHridoy = face_recognition.face_locations(imgHridoy)[0]
encodeHridoy = face_recognition.face_encodings(imgHridoy)[0]
cv2.rectangle(imgHridoy,(faceLocHridoy[3],faceLocHridoy[0]),(faceLocHridoy[1],faceLocHridoy[2]),(255,0,255),2)
# print(faceLoc)

faceLocHridoyTest = face_recognition.face_locations(imgHridoyTest)[0]
encodeHridoyTest = face_recognition.face_encodings(imgHridoyTest)[0]
cv2.rectangle(imgHridoyTest,(faceLocHridoyTest[3],faceLocHridoyTest[0]),(faceLocHridoyTest[1],faceLocHridoyTest[2]),(255,0,255),2)

"""(SRH) ---------RECOGNITION--TESING----------- (SRH)"""
results = face_recognition.compare_faces([encodeHridoy],encodeHridoyTest)
"""FOR BETTER MATCHING WE CAN USE DISTANCE"""
"""Distance besi hobe match na korle"""
faceDis = face_recognition.face_distance([encodeHridoy],encodeHridoyTest)
print(results,faceDis)
#displaying distance and matching result
cv2.putText(imgHridoyTest,f'{results} {round(faceDis[0],2)}', (50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

"""(SRH) ---------SHOWING IMAGES----------- (SRH)"""
cv2.imshow('Hridoy',imgHridoy)
cv2.imshow('HridoyTest',imgHridoyTest)
cv2.waitKey(0)


