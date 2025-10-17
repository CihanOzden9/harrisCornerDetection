import kenar_tespiti
import HC_methods
import images

image_list = images.get_images() #resimler

for img in image_list:
    print(img)
    edges = kenar_tespiti.edges(img) #Kenarları düzenlenmiş img
    if edges is not None:
        HC_methods.hcd_method(edges)



"""

HAFTAYA ÖDEV

Verilen parametrelerin değiştirilmesi
n adet fotoğrafta farklı parametreler ile time complexity analizi
dönüşüm doğruluk oranları analizi
manuel siyah beyaz filre kullanımı


"""