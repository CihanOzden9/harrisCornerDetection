import cv2
import matplotlib.pyplot as plt
%matplotlib qt


img = cv2.imread("nyc.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("orijinal"), plt.show()
# Ortalama Blur 
dst2  =cv2.blur(img, ksize=(3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Blur"), plt.show()

# Gaussian Blur
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gaussian Blur"), plt.show()

# Median Blur
mb = cv2.medianBlur(img, ksize=3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Median Blur"), plt.show()


