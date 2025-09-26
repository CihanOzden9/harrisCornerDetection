import cv2
import numpy as np

img = np.zeros((600,600,3), np.uint8) #siyah bir resim oluşturduk


# sırayla; resim - başlangı. noktası - bitiş noktası - rengi - kalınlığı

cv2.line(img,(120,0),(512,389),(0,255,0),3)



cv2.rectangle(img, (0,0),(256,256), (255,0,0), 3)


cv2.circle(img, (300,300), 50, (0,0,255), 2)

cv2.putText(img, "Deneme", (400,400), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))

cv2.imshow("All", img)

cv2.waitKey(0)