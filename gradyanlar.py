import cv2
import matplotlib.pyplot as plt
%matplotlib qt

img = cv2.imread("chess_table.jpg",0)

laplacian_img = cv2.Laplacian(img, ddepth= cv2.CV_16S)
plt.figure(), plt.imshow(laplacian_img, cmap="gray"), plt.axis("off")