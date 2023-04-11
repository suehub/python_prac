##fruits = []
##
##for _ in range(4) :
##    fruits.append(input("좋아하는 과일을 입력하세요 : "))
##
##print(fruits)
##
##if input("검색할 과일 이름 : ") in fruits :
##    print("당신이 좋아하는 과일입니다.")


##blist = ['Kim', 178, 'lee', 160]
##blist[0] = 'park'
##print(blist)
##
##for x in blist:
##    print(x)


##numbers = [92, 85, 96, 70, 73]
##total = 0
##for i in numbers :
##    total = total + i
##print("합계 =", total)


##population = ["서울", 9765, "부산", 3441, "인천", 2954]
##
##print("서울 인구 :", population[1])
##print("인천 인구 :", population[5])
##print("도서목록 : ", population[::2])
##print("인구의 합 : ", sum(population[1::2]))

#===================================================================
#===================================================================



### 오늘의 명언 출력하기
##
##import random
##
##saying = ['비교는 친구를 적으로 만든다.',
##          '분노는 바보들의 가슴속에서만 살아간다.',
##          '글은 병든 마음의 치유자와 같다.',
##          '사람은 사랑할 때 누구나 시인이 된다.',
##          '시작이 반이다.']
##
##today = random.choice(saying) # random.choice(리스트명) : 리스트에서 원소 랜덤 추출
##print("★ 오늘의 명언 ★")
##print(today)  



### 튜플 사용법 (최대값, 최소값, 평균, 정렬)
##
##numbers = (73, 64, 98, 57, 39, 79, 93, 87, 57, 69)
##
##print("최대값 :", max(numbers))
##print("최소값 :", min(numbers))
##print("평균 :", sum(numbers)/len(numbers))
##
##n_list = list(numbers)
##n_list.sort(reverse=True)
##print("정렬 :", tuple(n_list))



### 장바구니 리스트에 저장된 품목을 정렬해서 출력하기
##
##cart = ['사과', '화장지', '치약', '계란', '우유', '대파', '칫솔']
##
##cart.sort()
##
### 방법 1.
##n = 1
##for x in cart : # 파이썬에서는 반복문에 리스트를 사용하는 것을 더 추천.
##    print("[{0}] {1}".format(n, x))
##    # 0과 1은 순서 번호. 생략 가능. print("[", n, "]", x) 와 같음
##    n += 1 # no = no + 1
##    
### 방법 2.
####for x in range(len(cart)) :
####    print("[{}] {}".format(x+1, cart[x]))
##    
##print("------------------------------------")
##print("총 {}개 품목이 장바구니에 있습니다.".format(len(cart)))
### print("총", len(cart), "개 품목이 장바구니에 있습니다.")
##print("------------------------------------")




# 스크린 세이버 만들기
import random
import turtle as t

colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

t.pensize(5)
t.speed(10)

for _ in range(30) :
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    r = random.randint(50, 150)
    t.color(random.choice(colors))

    t.pu()
    t.goto(x, y)
    t.pd
    
    t.begin_fill()
    t.circle(r)
    t.end_fill()






