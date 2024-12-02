#문자열 포맷 서식 ->잘 안쓰는 형식
print("오늘은 %d%s %d일 입니다." %(12,'월',2)) 
print(f"오늘은 {12}{'월'} {2}일 입니다.") #잘 쓰는 형식!! ##
print("오늘은 " +str(12)+"월 "+str(2)+"일 입니다.") #가끔 쓰는 형식
print("오늘은 ",12,"월 ",2,"일 입니다.",sep='') #깔끔한 형식 ##

#대소문자 바꾸기-> 코딩테스트 단골문제!
print("Hello".upper())
print("Hello".lower())

#split() 굉장히 중요!!! 코딩테스트 상당히 많이 나옴!!!
friends = "고찬국 김다운 김민창"
a = friends.split()# ' '아무것도 안적으면 띄워쓰기가 default임
print(a)

sentence = "{}월 {}일".format(12,2) #12월 2일 {}안에 순서 없으면 차례대로 나오고 적으면 적은대로 나옴!
print(sentence)

b= "   111   222"
print(b.strip())
print(b.split())
print(b.replace("111","222"))

#실습2
print("<예제 입력>")
a=input('(1):')
b=input('(2):')
print('')

print("<예제 출력>")
c=int(a[:])*int(b[-1])
print(f"(3):{c}")

d=int(a[:])*int(b[1])
print(f"(4):{d}")

e=int(a[:])*int(b[0])
print(f"(5):{e}")

f=c+d*10+e*100
print(f"(6):{f}\n")

# 좀 더 좋은 코드
in1 = int(input("(1):"))
in2 = input("(2)")

print(in1*int(in2[2]))
print(in1*int(in2[1]))
print(in1*int(in2[0]))
print(in1*int(in2))