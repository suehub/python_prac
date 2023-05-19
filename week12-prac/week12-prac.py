import numpy as np
import matplotlib.pyplot as plt
import csv

##years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
##gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]
##
###plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
##plt.bar(years, gdp, width=5)
##plt.title("GDP per capita")
##plt.ylabel("dollars")
##plt.savefig("gdp.png", dpi=600)
##plt.show()

##x = ['a', 'b', 'c', 'd', 'e']
##y = [95, 69, 80, 73, 90]
##
##plt.title('Scores by Group')
##plt.xlabel('Group')
##plt.ylabel('Score')
##plt.grid()
##plt.scatter(x, y, color='red')
##plt.show()

##plt.rcParams['font.family'] = 'Malgun Gothic'
##times = [8, 14, 2]
##timelabels = ['잠자기', '공부하기', '놀기']
##
##plt.pie(times, labels=timelabels, autopct="%.2f")
##plt.show()

##books = [1, 6, 2, 3, 1, 2, 0, 2]
##plt.hist(books, bins=6)
##plt.xlabel('books')
##plt.ylabel('frequency')
##plt.show()



##x = np.arange(-10, 10) # 정수 생성
##y = 2*x
##
##plt.plot(x, y, marker='o') # plot은 선형 그래프
##
##plt.show()




#### 하나의 차트에 여러 데이터 표시하기
##
##years = [1960, 1970, 1980, 1990, 2000, 2010]
##ko = [130, 650, 2450, 11600, 17790, 27250]
##jp = [890, 5120, 11500, 42130, 40560, 38780]
##ch = [100, 200, 290, 540, 1760, 7940]
##
##xrange = np.arange(len(years))
##width = 0.3
##
##plt.bar(xrange-width, ko, width, label='Korea')
##plt.bar(xrange, jp, width, label='Japan')
##plt.bar(xrange+width, ch, width, label='China')
##plt.xticks(range(len(years)), years)
##plt.legend()
##plt.xlabel('years')
##plt.ylabel('GDP')
##plt.grid(True)
##
##plt.show()




#### 공공테이터포털의 활용
##
##data = np.genfromtxt('한국도로공사.csv', delimiter=',')
##
##x = data[1:, 0]  # 연도 슬라이싱
##y = data[1:, 1]  # 사고 건수
##
##plt.plot(x, y)
##
####plt.rcParams['font.family'] = 'Malgun Gothic'
####
####plt.figure(figsize=(12, 5), facecolor='lightyellow')
####plt.bar(x, y, width=0.5, color='darkgreen')
####plt.xlabel('Year')
####plt.ylabel('Number of accidents')
####plt.title('연도별 교통사고 통계')
##
##plt.show()




### 넘파이 난수 그래프
##
##x = np.arange(0, 1000)
##y = 3 * np.random.rand(1000) + 3  # 랜덤값 증폭과 이동 
##
##plt.figure(figsize=(10, 3))  # 가로세로 인치 사이즈
##plt.plot(x, y, marker='o', color='brown')
##plt.show()


### 정규분포 넘파이 난수 그래프
##
##x = np.random.randn(1000)
##y = np.random.randn(1000)  # randn은 정규분포 난수
##
##n = 20  # 구간(bin) -> 가로축 개수
##plt.hist(x, n, histtype='bar', color='red')
##plt.hist(y, n, histtype='bar', color='blue', alpha=0.5)   # alpha는 투명도 
##plt.show()



### 여러 가지 함수 차트
##
##x = np.arange(-20, 20) # 정수 생성
##y1 = 2*x
##y2 = x**2 + 5
##y3 = -(x**2) - 5
##
####plt.plot(x, y1, 'ro:')
####plt.plot(x, y2, 'g^-') 
####plt.plot(x, y3, 'b--*')
##plt.plot(x, y1,'ro:', x, y2,'g^-' ,x, y3, 'b*--')  # 3개의 함수 한 번에 작성
##
##plt.axis([-30, 30, -30,30]) # 축 범위 지정하기 (그릴 영역)
##plt.show()



# 하나의 그림에 여러 개의 그래프 그리기

x = np.random.randn(1000) * 2 + 50   # 표준 편차가 2, 평균이 50인 정규분포 난수
y = np.random.randn(1000)  # randn은 정규분포 난수

n = 10

plt.subplot(1, 2, 1) # 그림을 분리함. 121: 1행 2열을 첫번째 그림으로
plt.title('Data 1', fontsize=10)
plt.hist(x, n, histtype='bar', color='red')

plt.subplot(122)  # 1행 2열을 두 번재 그림으로
plt.title('Data 2', fontsize=10)
plt.hist(y, n, histtype='bar', color='blue')

plt.show()






















