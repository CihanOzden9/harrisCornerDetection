import cv2

img = cv2.imread("indir.jpeg", 1)

print(img.shape)

cv2.imshow("orijinal", img)

img_resized = cv2.resize(img,(500,300))

cv2.imshow("",img_resized)

cv2.waitKey(0)