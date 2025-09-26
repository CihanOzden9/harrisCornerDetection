import cv2
import matplotlib.pyplot as plt
import numpy as np

def gaussian_noisy(img):
    row, col, ch = img.shape
    mean = 0 #ortalama piksel değeri
    var = 0.05 #varyans değeri
    sigma = var ** 0.5 #sigma çarpanı
    
    #Random kötü piksel oluşturma
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    
    #Kötü pikselleri dağıtma
    gauss = gauss.reshape(row, col, ch)
    
    #Orijinal resme dönüştürme
    noisy_img = img + gauss
    
    return noisy_img

img = cv2.imread("nyc.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("orijinal"), plt.show()

noisy_img = gaussian_noisy(img)
plt.figure(), plt.imshow(noisy_img), plt.axis("off"), plt.title("gaussin"), plt.show()


gb = cv2.GaussianBlur(noisy_img, ksize=(3,3), sigmaX=7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("blur"), plt.show()


