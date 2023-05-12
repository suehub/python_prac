from wordcloud import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

##import collections      # 리스트, 딕셔너리, 튜플 등을 컬렉션이라고 함.
### 여기서는 리스트를 딕셔너리로 바꾸는 함수 사용.


##try :
##    f = open("frost.txt", "r")
##except :
##    print("파일을 확인하세요.")
##else :
##    text = f.read() # 공백을 기준으로 단어를 나눔. 개행 제거.
##    
##    f.close()
##
##    wc = WordCloud(background_color = 'white')
##    wc.generate_from_frequencies(text)  # generate_from_frequencies() : 빈도수 측정하여 시각화
##    wc.to_file('wc_image.png')  # 파일로 만들어서 저장



##try :
##    f = open("poem.txt", "r")
##except :
##    print("파일을 확인하세요.")
##else :
##    text = f.read() # 공백을 기준으로 단어를 나눔. 개행 제거.
##    
##    f.close()
##
##
##    icon = Image.open("mask.png", "r") # 이미지 파일 열기
##    mask = Image.new('RGB', icon.size, (255, 255, 255))  # 이미지 파일 변형
##    mask.paste(icon, icon)
##    mask = np.array(mask) # 이미지를 2차원 행렬로 변환
##
##
##    sw = STOPWORDS.union({'않고', '있으랴'}) # 불용어. 중지어
## 
##    wc = WordCloud(font_path = 'malgun', max_font_size = 200,
##                    background_color = 'white', width = 1200, height = 800,
##                    stopwords = sw, mask = mask) # stopwords는 불용어 처리
##    wc.generate(text)  # generate_from_frequencies() : 빈도수 측정하여 시각화
##    wc.to_file('wc_image.png')
##
##    plt.imshow(wc)  # 화면에 차트처럼 보여줌
##    plt.axis('off') # 그래프 가로세로 끄기
##    plt.show()



###### 파일에서 중복되지 않은 단어 개수 구하기 ######

wset = set()  # 집합은 중복 방지

try :
    f = open("dream.txt", "r")
except :
    print("파일을 확인하세요")
else :
    for line in f : # 파일을 한 줄씩 읽음
        wlist = line.split()
        for w in wlist :
            wset.add(w.lower())

    f.close()

    print("단어 개수 =", len(wset))

    print(wset)

##    count = 0
##    
##    for x in wlist :
##        if wlist.count(x) > 1 :
##            continue
##        count = count + 1
##        words.add(x)
    
    
















    
