import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #kamera en
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #kamera boy

print(width, height)

#kayıt için bellek oluşturduk
writer = cv2.VideoWriter("kayit-1.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20 ,(width, height)) 


while True:
    
    ret, frame = cap.read() #resimleri okumaya başladık
    
    cv2.imshow("Kayıt", frame) #kayıt ekranı açılıyor
    
    writer.write(frame) #çekilen resimler yazılıyor
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break #çıkış işlemi yapıyoruz

cap.release()
writer.release()
cv2.destroyAllWindows()