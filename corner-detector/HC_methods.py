import cv2
import numpy as np

def hcd_method(src_img):
    img = src_img

    if img is None:
        print("Img is not found.")
        return None

    # Eğer görüntü gri tonlamalıysa BGR'ye çevir
    if len(img.shape) == 2:
        color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        gray = np.float32(img)
        
    else:
        color_img = img.copy()
        gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)

    # Harris Corner Detection
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
    dst = cv2.dilate(dst, None)

    # Eşikleme ve köşeleri kırmızı ile işaretleme
    color_img[dst > 0.07 * dst.max()] = [0, 0, 255]  # BGR formatında kırmızı


    # Görüntüyü göster
    cv2.imshow("Harris Corner Detection", color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
