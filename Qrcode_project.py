import cv2
import numpy as np
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
myList = ['1111', '2222', '22267', 'https://wa.me/qr/3DVPJWEG4JR6H1']
while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        if myData in myList:
            myOutput = "Authorized"
            myColor = (0, 255, 0)
        else:
            myOutput = "Un-authorized"
            myColor = (0, 0, 255)




        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 10)
        pt2 = barcode.rect
        cv2.putText(img, myOutput, (pt2[0], pt2[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, myColor, 2)
    cv2.imshow("Result", img)
    cv2.waitKey(2)
