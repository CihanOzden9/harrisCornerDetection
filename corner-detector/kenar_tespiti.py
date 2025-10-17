import cv2
import numpy as np
import os
current_file = os.path.dirname(os.path.abspath(__file__))

def edges(src_img):
    img = cv2.imread(f"{current_file}/HCD_images/{src_img}", 0) #Orijinal siyah beyaz resim

    if img is None:
        print("Img is not found.(Edges)")
        return None
    img = cv2.resize(img,(500,500))

    #Blured uyguluyoruz su gibi nesnelerin kenarlarını kaldırmak için
    blured_img = cv2.blur(img, ksize = (2,2))

    img_median = np.median(blured_img)
    low = int(max(0, (1 - 0.5) * img_median))
    high = int(max(255, (1 + 0.5) * img_median))

    #Kenar tespit uygulaması
    edges = cv2.Canny(image = blured_img, threshold1 = low, threshold2 = high)

    return edges

