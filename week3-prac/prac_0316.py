# 변수를 echo로 확인하면 문자열이 ' '로 출력. print는 값만 출력해줌
# 코드 클릭 엔터 -> 불러오기


###############################################
### 키보드로 입력한 두 정수의 합계를 출력하기 #
###############################################
##
##number1 = int(input('첫 번째 정수를 입력해주세요 : '))
##number2 = int(input('두 번째 정수를 입력해주세요 : '))
##
##print(number1, '과', number2, '의 합계는', number1+number2, '입니다.')


##############
# bmi 계산기 #
##############
##
##name = input('이름 입력 : ')
##w = float(input('몸무게 입력(kg) : '))
##h = float(input('키 입력(cm) : ')) 
##bmi = w/(h/100)**2
##print(name, '님의 BMI는', bmi, '입니다.') 


# % : 나머지, // : 몫.
# 연산자 우선순위 : 괄호 > 산술(** > *,/,%,// > +,-) > 비교 > 논리


#####################
# 거스름돈 계산하기 #
#####################
##
##pencil = 400
##money = int(input('가진 돈은 몇 원? : '))
##print('연필은', money//pencil, '자루')
##print('거스름돈은', money%pencil, '원')



#################
# 시간 계산하기 #
#################
##
##time = int(input('계산할 시간(초)을 입력 : '))
##
##hour = time // 60 // 60
##minute = time // 60 % 60
##second = time % 60
##
##hour = time // 3600
##minute = (time % 3600) // 60
##second = (time % 3600) % 60
##
##print(hour, '시간', minute, '분', second, '초입니다.')



# 제곱 연산자는 오른쪽부터 계산

#####################
# 피타고라스의 정리 #
#####################

a = float(input('직각삼각형이 밑변 : '))
b = float(input('직각삼각형의 높이 : '))
c = (a**2 + b**2)**(1/2)
#c = (a**2 + b**2)**0.5

print('빗변은', c, '입니다.')

 


















