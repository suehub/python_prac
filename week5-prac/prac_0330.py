### 1~100까지 출력
##x = 0
##    x = x + 1
##    print(x, end=" ") # end=" " : 한 줄로 출력
##
##print()
##
### 1~100까지 홀수만 출력
##x = 0
##while x < 100 :
##    x = x + 1
##    if x % 2 != 0 :
##        print(x, end=" ")


### 양수를 하나 입력하고(num) 1부터 num까지 출력
##x = 1
##num = int(input("양수 입력 : "))
##while x <= num :
##    print(x, end=" ")
##    x = x + 1
##
##print()
##
### 양수를 하나 입력하고(num) 1부터 num까지 홀수만 출력
##x = 1
##while x <= num :
##    print(x, end=" ")
##    x = x + 2


##num = int(input("양수 입력 : "))
##x = 0
##while True :
##    x = x + 1
##    if x > num : break           # break : 반복문을 끝냄
##    if x % 3 == 0 : continue     # continue : 반복문을 건너뜀
##    print(x, end=" ")



### 숫자 맞히기 게임
##import random
##
##com = random.randint(1, 20)
##print("***게임을 시작합니다.***")
##
##while True :
##    num = int(input("숫자 입력(1~20) : "))
##
##    if num < 1 or num > 20 :
##        print("잘못된 범위의 숫자를 입력하셨습니다.")
##        # continue는 작성하지 않아도 됨.
##    elif num > com :
##        print("↙")
##    elif num < com :
##        print("↖")
##    else :
##        print("★정답★")
##        break
##            
##print("***게임을 종료합니다.***")   
##


### while문을 for문으로 
##x = 0
##while x<=4 :
##    print(x, end=" ")
##    x = x + 1
##x = 0
##for x in range(5) :
##    print(x, end=" ")





# 구구단 출력하기
dan = int(input("몇 단을 출력할까요? : "))

for x in range(1, 10) :
    print(dan, "X", x, "=", dan*x)



