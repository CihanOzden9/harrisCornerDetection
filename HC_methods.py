import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

#resmi içe aktar
img = cv2.imread("hc_img(2).jpg")

#grayformata çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#Harris methodunu uygula
hc_method = cv2.cornerHarris(gray, blockSize = 2, ksize = 3, k = 0.04)
dst = cv2.dilate(hc_method, None)

#köşeleri işaretle
img[dst > 0.02 * dst.max()] = [255,0,0]

#yazdır
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")