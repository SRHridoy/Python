import os

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
# print(listShirts)
fixedRatio = 262/190#Width of shirt /width of point11 to 12
shirtRatioHeightWidth = 581/440

while True:
    success, img = cap.read()
    # This is getting image from the pose
    img = detector.findPose(img)
    #img = cv2.flip(img,1)
    # Here we can get landmarkList and bounding box info
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmList:
        #center = bboxInfo["center"]
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]
        imgShirt = cv2.imread(os.path.join(shirtFolderPath,listShirts[0]),cv2.IMREAD_UNCHANGED)


        widthOfShirt = int((lm11[0] - lm12[0])*fixedRatio)
        print(widthOfShirt)
        imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt*shirtRatioHeightWidth)))
        currentScale = (lm11[0] - lm12[0]) / 190
        offset = int(44 * currentScale), int(48 * currentScale)
        try:
            img = cvzone.overlayPNG(img,imgShirt,(lm12[0]-offset[0],lm12[1]-offset[1]))
        except:
            pass

    cv2.imshow("Shirt Trial Mirror",img)
    cv2.waitKey(1)
