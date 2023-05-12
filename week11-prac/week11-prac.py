#### BMI 계산하기
##import numpy as np
##
##heights = [183, 176, 169, 186, 177, 173]
##weights = [86, 74, 59, 95, 80, 68]
##
##np_heights = np.array(heights)
##np_weights = np.array(weights)
##
##bmi = np_weights / (np_heights/100) ** 2
##
##print('대상자들의 키 :', heights)
##print('대상자들의 몸무게 :', weights)
##print('대상자들의 BMI')
##print(bmi)


#### 2차원 배열에서 원하는 조건의 정보 찾기
##import numpy as np
##
##players = [[170, 76.4],
##           [183, 86.2],
##           [181, 78.5],
##           [176, 80.1]]
##
##np_players = np.array(players)
##
##print('몸무게가 80 이상인 선수 정보')
##print(np_players[np_players[:, 1] >= 80])
##
##print('키가 180 이상인 선수 정보')
##print(np_players[np_players[:, 0] >= 180])
##
### BMI가 25 이상인 선수 정보만 출력하기
### bmi = w/h**2
##bmi = np_players[:, 1] / (np_players[:, 0]/100) ** 2
##
##print('BMI가 25 이상인 선수 정보')
##print(np_players[bmi >= 25])


#### 교통사고통계 분석
##import numpy as np
##
##data = np.genfromtxt('교통사고통계.csv', delimiter = ',')
##
##count = data[:, 1]
##
##print('연간 교통사고 평균 :', np.mean(count))


## 난수를 만드는 함수
# np.random.seed(100) # seed 설정은 동일한 난수값을 생성
# np.random.rand(5)   # rand는 매번 다른 난수값 생성


#### 범위를 입력하면 해당 범위의 난수를 10개 만들기
##import numpy as np
##
##start = int(input('난수 생성 범위의 시작 값은? : '))
##end = int(input('난수 생성 범위의 종료 값은? : '))
##
### np.random.rand(10)                  -> 0~1 사이 난수 10개 생성
### 100 * np.random.rand(10)            -> 0~100 사이 난수 10개 생성
### (100-50) * np.random.rand(10)       -> 0~50 사이 난수 10개 생성
### (100-50) * np.random.rand(10) + 50  -> 50~100 사이 난수 10개 생성
##
##print((end - start) * np.random.rand(10) + start) # end-start 가 증폭되는 범위임



## 인구 분석
import numpy as np


data = np.genfromtxt('인구.csv', delimiter = ',')
# np는 숫자데이터를 다루기 때문에 제목(문자열)을 읽어오지 못함 -> 맨 위 두 줄 지우기
# 데이터는 실수형임 -> 정수형으로 바꾸기
data = data[2:, :].astype(int)


year = int(input('검색할 연도는? : '))

result = data[data[:,0] == year]

for x, y in result :  # 결과가 리스트이기 때문에 반복문 사용하여 출력
    print('{}년 인구는 {:,}명입니다.'.format(x, y))






























