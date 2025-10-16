import cv2
import numpy as np

# Kamerayı aç (0 = varsayılan kamera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: #Kamera algılanmadıysa
        print("Connect could not be established!")
        break
    
    frame = cv2.flip(frame,1)

    # Gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Harris Corner Detection
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Köşe noktalarını daha belirgin yapmak için genişlet
    dst = cv2.dilate(dst, None)

    # Eşikleme: güçlü köşeleri kırmızı ile işaretle
    frame[dst > 0.02 * dst.max()] = [0, 255, 0]

    # Sonucu göster
    cv2.imshow("Real time harris corner detection", frame)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
