import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread("chess_table.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# float32 tipine dönüştürmek gerekiyor
gray = np.float32(gray)

# Harris köşe algılama
# blockSize: köşe algılamada kullanılacak komşu boyutu
# ksize: Sobel türev filtresi boyutu (standart)
# k: Harris dedektör sabiti (0.04 - 0.06 arası genelde kullanılır)
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Sonuçları genişletmek için dilate uyguluyoruz
dst = cv2.dilate(dst, None)

# Köşeleri işaretleme (eşik değerine göre kırmızı renk veriyoruz)
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Sonucu göster
cv2.imshow("Harris Corner Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
