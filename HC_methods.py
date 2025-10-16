import cv2
import numpy as np
import matplotlib.pyplot as plt
import images
#%matplotlib qt

def hcd_method(src_img):
    #resmi içe aktar
    img = cv2.imread(fr"HCD_images\{src_img}")

    if img is None:
        print(f"{src_img} okunamadı")
        return 0

    #grayformata çevir
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    #Harris methodunu uygula
    hc_method = cv2.cornerHarris(gray, blockSize = 2, ksize = 3, k = 0.04)
    dst = cv2.dilate(hc_method, None)

    #köşeleri işaretle
    img[dst > 0.02 * dst.max()] = [255,0,0]
    img = cv2.resize(img,(500,500))

    cv2.imshow(f"{src_img} harris corner detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


images = images.get_images()
for img in images:
    hcd_method(img)