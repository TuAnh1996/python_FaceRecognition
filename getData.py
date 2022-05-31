import cv2
import numpy as np
import sqlite3  # để kết nối làm vc với database
import os  # để truy cập đc vào các đường dẫn trong máy

# mình sẽ tạo dataSet dùng để nhận diện
# viết hàm truy cập tới database sqliteKết nối sqlite để tạo/cập nhật record
# insertOrUpdate(ID,NAME,AGE) có nghĩa mình sẽ truyền cái id name age vào xong nó chạy vào hàm này để ktraa


def insertOrUpdate(id, name, age):  # insertOrUpdate thêm mới hoặn update
   # data.db mình tạo trc đó nhờ vào DB sqlite
    # connect truy cấp  tới data base triy cập tới đường dẫn chứa data base
    conn = sqlite3.connect('data.db')

    # ktra id nhập vào có hay chưa

    # viết lệnh xem id đã đc nhập vào hay chưa,rồi thì inser chưa thì update
  # Lệnh SELECT: Lấy các bản ghi cụ thể từ một hoặc nhiều bảng.
  # Xác định cột có giá trị muốn lấy: SELECT cot1, cot2, cotN FROM ten_bang;
  # còn phía dưới trên tất cả các cột trong bảng
    query = "SELECT * FROM Student WHERE ID =" + str(id)
    # Phương thức execute sẽ sử dụng câu lệnh SQL lấy tấ dữ liệu của table là “Select * from table_name”,
    # chúng ta lấy một đối tượng Cursor, đối tượng này làm nhiệm vụ duyệt qua các bản ghi trong tập dữ liệu được lấy về và thực thi các câu truy vấn. Để thực thi một câu truy vấn thì chúng ta dùng phương thức execute().
    cursor = conn.execute(query)
    # thực thi câu truy vấn lấy thông tin

    # Chúng ta chỉ cần dùng phương thức execute() để thực thi các câu lệnh SQL
    isRecordExist = 0  # đẻ ktra id trg dât nếu có cho bằng 1 nếu chưa cho bằng 0 update
    for row in cursor:  # cái này cursor nó trả về 1 list
        isRecordExist = 1  # tức nó tồn tại
        # print(row)
    # SQL INSERT INTO database_name VALUES(components)để thêm giá trị.  Tạo một bản ghi.
    if(isRecordExist == 0):
      #  xác định cột dể chèn INSERT INTO TABLE_TEN (cot1, cot2, cot3,...cotN)]  VALUES (giatri1, giatri2, giatri3,...giatriN);
        query = "INSERT INTO Student (ID,Name,Age) VALUES(" + \
            str(id) + "," + str(name) + "," + str(age) + ")"
    else:  # tức có mình phải update
        query = "UPDATE Student SET Name=" + \
            str(name) + "Age=" + str(age) + "WHERE ID=" + str(id)
    conn.execute(query)
    conn.commit()
    conn.close()
# insertOrUpdate(1,"abc")1


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Dòng này là khai báo 1 lớp nhận diện khuôn mặt lưu vào 1 biến
cap = cv2.VideoCapture(0)
# is để ng dùng nhập id vs nam
ID = input("ENter your Id :")
NAME = input("Enter your Name :")
AGE = input("Enter your Age :")
insertOrUpdate(ID, NAME, AGE)

sampleNum = 0
# có lỗi sqlite3.OperationalError: no such column: tu thì chữ tú đó phải cho vào ngoặc "tuq"
while True:
    res, frame = cap.read()  # cái này đọc dữ liệu từ webcam
    # res neesu truy cap thanhf công nó sẽ trả về true
    # còn frame là dữ liệu mình có đc ở đay là img

    # mình phải chuyển ảnh sang ảnh sáng để train truyển sang màu sáng
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # sau khi lấy đc màu ảnh thfi mình sd thư việc detec tức truy cập vào để kết hợp thư viện để nhận dạng mặt
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # sau đó vẽ hình vuông bao quyanh 3
    for (x, y, w, h) in faces:
        # rectangle giúp vẽ đc hình vuông trong webcam,frame hình ảnh lấy đc
        # 255, 0, 0 màu hình vuông còn số 2 là độ dày
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        if not os.path.exists("dataSet"):
            os.makedirs("dataSet")
        sampleNum += 1
        # chú ý cái ID này chính là id mình yêu cầu nhập về ở trên ID = input("ENter your Id :")
        cv2.imwrite("dataSet/User" + str(ID) + "." +
                    str(sampleNum) + ".jpg", gray[y: y+h, x:x+w])
    cv2.imshow('img', frame)  # sau khi có đc mình show nó đi "img" là tiêu đề
    # để dịch chuyển cái ô vùng vào mặt mình

    # waitkey là hàm đợi đến khi nào có
    #k = cv2.waitKey(30) & 0xff6
    k = cv2.waitKey(1)
    # if k==27:
    #   break
    if sampleNum > 50:
        break
    # Khi bật camera lên vào mỗi vòng lặp while nó sẽ chụp 1 bức hình phân tích nếu k lặp đến lần thứ 27 thid dừng
cap.release()  # xosa bộ nhớ sau khi đc
cv2.destroyAllWindows()
