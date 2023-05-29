##import matplotlib.pyplot as plt
##import matplotlib.image as mpimg
##img = mpimg.imread('mandrill.png')
##print(img)
##
##image_plot = plt.imshow(img)
##plt.show()


##import cv2
##
##img = cv2.imread('candles.jpg')
##
##img2 = cv2.imread('candles.jpg', cv2.IMREAD_GRAYSCALE)
##
##cv2.imwrite('candles_gray.jpg', img2)


##import cv2
##import sys 
##
##img = cv2.imread('mandrill.png')
##if img is None :
##    print("image load falled!")
##    sys.exit()
##    
##cv2.namedWindow('image')
##cv2.imshow('image', img)
##
##while True :
##    if cv2.waitKey() == ord('q') :
##        break
##
##cv2.destroyWindow('image')


##import cv2
##
##img_files = ['bag.png', 'candles.jpg', 'iceberg.jpg', 'salt.png', 'shoes.png']
##
##
##cv2.namedWindow('image', cv2.WINDOW_NORMAL)
##cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
##
##i = 0
##cnt = len(img_files)
##
##while True :
##    img = cv2.imread(img_files[i])
##    cv2.imshow('image', img)
##    if cv2.waitKey(1000) == 27 :
##        break
##    
##    i += 1
##    if i >= cnt :
##        i = 0



##import cv2
##img = cv2.imread('mandrill.png', cv2.IMREAD_GRAYSCALE)
##img2 = cv2.resize(img, (50, 50))
##img3 = img[:, :128]
##img4 = cv2.blur(img, (10, 10))
##img5 = cv2.imread('salt.png', cv2.IMREAD_GRAYSCALE)
##img6 = cv2.medianBlur(img, 3)
##img7 = cv2.equalizeHist(img)
##
##
##cv2.imshow('original', img5)
##cv2.imshow('resized', img2)
##cv2.imshow('cropped', img3)
##cv2.imshow('blurred', img6)
##cv2.imshow('equalized', img7)
##
##cv2.waitKey()
##cv2.destroyAllWindows()




#### 도형 그려보기
##import cv2

##img = cv2.imread('image/mandrill.png', 0)   # flags : (0 : GRAYSCALE, 1 : COLOR)
##img2 = cv2.imread('image/mandrill.png', 1)
##
##cv2.imshow('grayscale', img)
##k = cv2.waitKey()
##if k == 27 :   # 27 : Esc
##    cv2.imshow('color', img2)
##cv2.destroyWindow('grayscale')
##cv2.waitKey()
##cv2.destroyAllWindows()

##img = cv2.imread('image/mandrill.png', 1)
##
##cv2.line(img, (0,0), (250,250), (255,0,0), 5)
##cv2.arrowedLine(img, (0,250), (250, 0), (0,255,0), 5)
##cv2.rectangle(img, (20, 230), (230, 20), (0, 0, 0), 5)
##cv2.putText(img, 'Hello', (100,100), fontFace=1, fontScale=4, color=(255,255,255))   # fontFace : 글자 모양(0~6)
##
##cv2.imshow('shaped', img)





#### 트랙바로 이미지 명암 조절하기
##
##import cv2
##
##img = cv2.imread('image/mandrill.png', 0)
##cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
##
##def change_bright(x) :
##    cv2.imshow('image1', img+x)
##
##cv2.createTrackbar('bright', 'image1', 0, 100, change_bright)





## 이미지의 특정 색상 영역을 추출하기

import cv2
import numpy as np


img = cv2.imread('image/green_back.png')
cv2.imshow('Original', img)  # 원본

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # HSV 색 공간 변환. 오차 범위를 더 줄여줌

min_green = np.array([40,50,50]) # 녹색 하한값. (색상, 채도, 명도)
max_green = np.array([80,255,255]) # 녹색 상한값

img2 = cv2.inRange(img, min_green, max_green)
cv2.imshow('Green Area', img2)
































