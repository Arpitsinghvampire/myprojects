import cv2
import matplotlib.pyplot
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    edges=cv2.Canny(img,100,200,3,L2gradient=True)
    cv2.imshow('canny edges',edges)
    if cv2.waitKey(1) &0xFF==ord('q'):
        break
cap.release()q
cv2.destroyAllWindows()