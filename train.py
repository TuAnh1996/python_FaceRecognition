import cv2
import numpy as np
import os
from PIL import Image  # để trích xuât đc ảnh từ thư mục
 # sau khi mình thêm 1 ng mới ta có đc ảnh ng đó nếu cta k train dữ liệu thì dữ liệu sẽ k có khi ta nhận diện ng đó thì sẽ k nhận diện đc vậy nene sau khi chụp ta phải train dữ liệu
 
# bước để Training từ file ảnh thu đc để traing
#bước này để mình có đc data dữ liệu
# đê traing đc ta cần lấy đc id ra
recognizer = cv2.face.LBPHFaceRecognizer_create()


# lấy đường dẫn
path = "dataSet"
# hàm đẻ lấy id và list


def getImageWithId(path):
     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
     #print(imagePaths)  # mình gọi hàm nó sẽ in ra tất cả các đường dẫn ảnh
     # h mình sẽ tạo 2 mảng id và face đẻ lấy tất cả các ảnh và dữ liệu
     faces = []
     IDs=[]
     for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        print(faceNp)# nó in ra 1 mảng dữ liệuuu
        # split to get ID of the image
        Id = int(imagePath.split("\\")[1].split('.')[1])
        faces.append(faceNp)
        #print ID
        IDs.append(Id)
        cv2.imshow("traning",faceNp)
        cv2.waitKey(10)
     return IDs, faces
Ids,faces=getImageWithId(path)
#trainning
recognizer.train(faces,np.array(Ids))
if not os.path.exists('recognizer'):
     os.makedirs('recognizer')
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
