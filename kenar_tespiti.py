import cv2
import matplotlib.pyplot as plt
import numpy as np
%matplotlib qt

img = cv2.imread("london.jpeg", 0) #Orijinal siyah beyaz resim
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

#Blured uyguluyoruz su gibi nesnelerin kenarlarını kaldırmak için
blured_img = cv2.blur(img, ksize = (2,2))

img_median = np.median(blured_img)
low = int(max(0, (1 - 0.33) * img_median))
high = int(max(255, (1 + 0.33) * img_median))

edges = cv2.Canny(image = blured_img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")