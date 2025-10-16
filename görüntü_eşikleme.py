import cv2

img = cv2.imread("images/tree.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("orijinsl", img)

_, thresh_img  =cv2.threshold(img, thresh = 135, maxval = 255, type = cv2.THRESH_BINARY)

cv2.imshow("Deneme", thresh_img)
cv2.waitKey(0)