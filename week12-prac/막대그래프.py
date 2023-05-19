## 국민소득에 대한 다중 막대형 그래프 그리기

import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

plt.bar(years, gdp, width=5, color='green') # 막대형 그래프
plt.title("GDP per capita")
plt.ylabel("dollars") # y축 제목
plt.savefig("gdp.png", dpi=600) # 이미지 파일로 저장
plt.show()
