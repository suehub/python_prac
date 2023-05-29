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


import cv2

img_files = ['bag.png', 'candles.jpg', 'iceberg.jpg', 'salt.png', 'shoes.png']


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

i = 0
cnt = len(img_files)

while True :
    img = cv2.imread(img_files[i])
    cv2.imshow('image', img)
    if cv2.waitKey(1000) == 27 :
        break
    
    i += 1
    if i >= cnt :
        i = 0



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




























