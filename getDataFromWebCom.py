import cv2
import numpy as np
# hỗ trợ thao tác ,truy xuất nhanh hơi,đc tối ưu hóa khi là vc vs cpu 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Dòng này là khai báo 1 lớp nhận diện khuôn mặt lưu vào 1 biến
cap = cv2.VideoCapture(0)
# để truy cập vafp camera
# dòng này dùng để mở camera ,o ở đây là tùy loại camera sẽ truyền các gtri khac nhau vì mình dùng của lap nên o
while True:
    res,frame = cap.read()# cái này đọc dữ liệu từ webcam
    #res neesu truy cap thanhf công nó sẽ trả về true
    #còn frame là dữ liệu mình có đc ở đay là img

    #mình phải chuyển ảnh sang ảnh sáng để train truyển sang màu sáng
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #sau khi lấy đc màu ảnh thfi mình sd thư việc detec tức truy cập vào để kết hợp thư viện để nhận dạng mặt 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #sau đó vẽ hình vuông bao quyanh 
    for (x, y, w, h) in faces:
        #rectangle giúp vẽ đc hình vuông trong webcam,frame hình ảnh lấy đc
        # 255, 0, 0 màu hình vuông còn số 2 là độ dày
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', frame)# sau khi có đc mình show nó đi "img" là tiêu đề
    # để dịch chuyển cái ô vùng vào mặt mình 

    #waitkey là hàm đợi đến khi nào có 
    #k = cv2.waitKey(30) & 0xff
    k = cv2.waitKey(1) & 0xFF
    #if k==27:
     #   break
    if k== ord("q"):
        break 
    #Khi bật camera lên vào mỗi vòng lặp while nó sẽ chụp 1 bức hình phân tích nếu k lặp đến lần thứ 27 thid dừng
cap.release()#xosa bộ nhớ sau khi đc
cv2.destroyAllWindows()