## *** 텍스트 파일 읽기 ***
##num = 0
##with open("dream.txt", "r") as f :
##    while True :
##        s = f.readline()
##        if s == "" : break  # ""은 빈 문자열.
##        num = num + 1
##        print(num, ":", s, end="")


##f = open("dream.txt", "r")
###contents = f.readlines() # 한 줄 씩 리스트형으로 저장
##for contents in f :  # file명을 for문 안에 작성하면 한 줄 씩 출력 가능
##    print(contents.rstrip())  # print는 자동으로 줄 바꿔줌. rstrip은 right strip. 문자열 오른쪽 불필요한 특수기호 제거
##f.close()




## *** 텍스트 파일에 쓰기 ***
# 문자열 쓰기는 바이너리 파일도 가능.
##f = open("guest.txt", "w")
##
####f.write("boo\n")
####f.writelines("kim\n" "lee\n" "park\n" "choi\n")
####f.writelines(["123\n", "456\n", "789\n"])
####f.write(str(100)+"\n")    # 숫자는 문자열로 형변환해서 써야 함
####f.write(str(101)+"\n")
##
####contents = input("파일에 쓸 내용은? : ")
####f.write(contents + "\n")
##f.write(input("파일에 쓸 내용은? : ") + "\n")
##
##f.close()
##print('파일 저장 완료!')


##f = open("score.txt", "w")
##print("점수를 입력하세요. 음수를 입력하면 프로그램이 종료됩니다.")
##
##while True :
##    score = input("점수 : ")
##    if int(score) < 0 :
##        break
##    f.write(score+"\n")
####    score = int(input("점수 : "))
####    if score < 0 :
####        break
####    f.write(str(score)+"\n")
##
##f.close()
##print("입력을 종료합니다.")


## *** 예외처리 ***
##try :
##    f = open("dream.txt", "r")
##except :
##    print("파일을 열기 오류!!")
##else : 
##    print(f.read())
##    f.close()
##    
##print("프로그램 종료")

##try :
##    number = int(input("정수 입력 : "))
##except :
##    print("정수를 입력하세요.")
##else :
##    print(number**5)
##    
##print("프로그램 종료")


## 예외처리 활용 프로그램
f = open("score.txt", "w")
print("점수를 입력하세요. 음수를 입력하면 프로그램이 종료됩니다.")

while True :
    try :
        score = int(input("점수 : "))
        
    except :
        print("정수값으로 입력해야 합니다! 다시 입력하세요.")
    else :
        if score < 0 :
            break
        f.write(str(score) + "\n")
##    score = input("점수 : ")
##    try :
##        if int(score) < 0 :
##            break
##    except :
##        print("정수값으로 입력해야 합니다! 다시 입력하세요.")
##    else :
##        f.write(score + "\n")

f.close()
print("입력을 종료합니다.")




