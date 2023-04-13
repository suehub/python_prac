### 중간고사 
# 오늘까지 배운 것 1시간 동안 문제 5-6개 풀고 이러닝으로 제출. 퀴즈 형식
# 수업 자료나 검색 가능. 코드, 필기도 옮겨놓으면 가능.
# 수업 실습 내용과 비슷. 

########### 7장 데이터 탐색 ############

### 편의점 재고 관리 프로그램
##
##items = {"커피음료":7, "펜":3, "종이컵":2, "우유":1, "콜라":4, "책":5}



### 파티에 한 번만 참석자 찾기
##partyA = set(["Park", "kim", "Lee"])
##partyB = set(["Park", "Choi"])
##
##print("각 파티에 한 번만 참석한 사람은 다음과 같습니다.")
##print(partyA ^ partyB)





## 딕셔너리에 연락처 정보 저장하기

contact = {"엄마":"010-5035-9300", "아빠":"010-5381-2040", "오빠":"010-8761-9812"}


for x, y in contact.items() :
    print(x, ':', y)

##name = input("***이름 입력 : ")
##
### print(contact.get(name))
##if name in contact :    # print(contact.get(name))
##    print(name, "의 번호는", contact.get(name), "입니다.")
##else :
##    print("이름이 존재하지 않습니다.")


## 연락처 추가
name, phone = input("연락처 추가(이름 전화번호) : ").split() # split은 빈칸을 기준으로 나눔

if name in contact :
    confirm = input("기존 연락처가 있습니다. 변경할까요?(y/n) : ")
    if(confirm == 'y') :
        contact[name] = phone ######## 딕셔너리에 추가나 변경하는 것 중요함 #####
        print(name, "님의 연락처는", phone)
else :
    contact[name] = phone
    print("추가 완료!!")

for x, y in contact.items() :
    print(x, ':', y)



































