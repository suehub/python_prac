dic = []

print("문장을 입력하면 단어를 등록합니다(종료는 0) :")

while True :
    sentence = input("문장 입력 : ")
    if sentence == '0' :
        break

    words = sentence.split()
    
    for x in words :
        if x not in dic :
            dic.append(x)

print("***** 단어 사전 *****")
for x in sorted(dic) :
    print(x)
