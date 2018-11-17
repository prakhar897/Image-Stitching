from func import Main
import imutils
import cv2

Firstimage = cv2.imread("./images/ans01.jpg")
Secondimage = cv2.imread("./images/2.jpg")
Firstimage = imutils.resize(Firstimage, width=640)
Secondimage = imutils.resize(Secondimage, width=640)
Firstimage= cv2.copyMakeBorder(Firstimage,100,100,100,100,cv2.BORDER_CONSTANT,value=0)
Secondimage= cv2.copyMakeBorder(Secondimage,100,100,100,100,cv2.BORDER_CONSTANT,value=0)


obj = Main()
(Result, vis) = obj.stitch([Firstimage, Secondimage], showMatches=True)

# show the images
cv2.imshow("Image A", Firstimage)
cv2.imshow("Image B", Secondimage)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", Result)
cv2.imwrite("ans.jpg",Result)
cv2.waitKey(0)